
import json
import math
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

import matplotlib.pyplot as plt # type: ignore


def to_float(value, default=None):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def get_point(obj):
    if not isinstance(obj, dict):
        return None

    x = to_float(obj.get("x"))
    y = to_float(obj.get("y"))

    if x is None or y is None:
        return None

    return {"x": x, "y": y}


def iter_values_as_list(obj):
    if isinstance(obj, dict):
        return list(obj.values())
    if isinstance(obj, list):
        return obj
    return []


def line_length(p1, p2):
    return math.hypot(p2["x"] - p1["x"], p2["y"] - p1["y"])


def line_midpoint(p1, p2):
    return {
        "x": (p1["x"] + p2["x"]) / 2,
        "y": (p1["y"] + p2["y"]) / 2,
    }


def offset_point(p, dx, dy):
    return {"x": p["x"] + dx, "y": p["y"] + dy}


def normalize_vector(dx, dy):
    length = math.hypot(dx, dy)
    if length == 0:
        return 0.0, 0.0
    return dx / length, dy / length


def perpendicular_vector(p1, p2):
    dx = p2["x"] - p1["x"]
    dy = p2["y"] - p1["y"]
    ux, uy = normalize_vector(dx, dy)
    return -uy, ux


def draw_line(ax, p1, p2, color="black", lw=1.0, zorder=2, linestyle="-"):
    ax.plot(
        [p1["x"], p2["x"]],
        [p1["y"], p2["y"]],
        color=color,
        linewidth=lw,
        zorder=zorder,
        linestyle=linestyle,
    )


def draw_text(ax, x, y, text, fontsize=8, color="black", rotation=0, zorder=5):
    ax.text(
        x,
        y,
        text,
        fontsize=fontsize,
        color=color,
        ha="center",
        va="center",
        rotation=rotation,
        bbox=dict(facecolor="white", edgecolor="none", pad=0.2, alpha=0.75),
        zorder=zorder,
    )


def polygon_centroid(points):
    if not points:
        return None

    if len(points) == 1:
        return points[0]

    x_sum = 0
    y_sum = 0
    n = 0

    for p in points:
        pt = get_point(p) if not isinstance(p, dict) or "x" not in p else p
        if pt:
            x_sum += pt["x"]
            y_sum += pt["y"]
            n += 1

    if n == 0:
        return None

    return {"x": x_sum / n, "y": y_sum / n}


def point_on_segment(p1, p2, dist):
    total = line_length(p1, p2)
    if total == 0:
        return {"x": p1["x"], "y": p1["y"]}
    t = dist / total
    return {
        "x": p1["x"] + (p2["x"] - p1["x"]) * t,
        "y": p1["y"] + (p2["y"] - p1["y"]) * t,
    }


def draw_arc(ax, center, radius, start_angle, end_angle, steps=40, color="gray", lw=0.8):
    if steps <= 0:
        return

    angles = []
    if end_angle >= start_angle:
        step = (end_angle - start_angle) / steps
        angles = [start_angle + i * step for i in range(steps + 1)]
    else:
        step = (start_angle - end_angle) / steps
        angles = [start_angle - i * step for i in range(steps + 1)]

    xs = [center["x"] + radius * math.cos(a) for a in angles]
    ys = [center["y"] + radius * math.sin(a) for a in angles]
    ax.plot(xs, ys, color=color, linewidth=lw, zorder=4)


def clean_room_name(value):
    if value is None:
        return ""
    text = str(value).strip()
    if text.lower() in ("none", "null", "undefined"):
        return ""
    return text


def collect_rooms(plan):
    rooms = []

    raw_rooms = plan.get("rooms2") or plan.get("rooms") or []
    for room in iter_values_as_list(raw_rooms):
        if not isinstance(room, dict):
            continue

        area = room.get("area")
        name = clean_room_name(room.get("name") or room.get("title") or room.get("label") or "")

        center = get_point(room.get("pc")) or get_point(room.get("center"))

        polygon = room.get("polygon") or room.get("points") or []
        poly_points = []

        if isinstance(polygon, list):
            for p in polygon:
                pt = get_point(p)
                if pt:
                    poly_points.append(pt)

        if center is None and poly_points:
            center = polygon_centroid(poly_points)

        rooms.append({
            "area": to_float(area),
            "name": name,
            "center": center,
            "polygon": poly_points,
        })

    return rooms


def collect_walls(plan):
    walls = []

    raw_walls = plan.get("walls2") or plan.get("walls") or []
    for wall in iter_values_as_list(raw_walls):
        if not isinstance(wall, dict):
            continue

        p1 = get_point(wall.get("p1") or wall.get("a") or wall.get("start"))
        p2 = get_point(wall.get("p2") or wall.get("b") or wall.get("end"))

        if not p1 or not p2:
            continue

        depth = to_float(wall.get("depth"), 120)

        holes = []
        raw_holes = wall.get("holes") or wall.get("windows") or wall.get("doors") or []
        for hole in iter_values_as_list(raw_holes):
            if not isinstance(hole, dict):
                continue

            hp1 = get_point(hole.get("p1") or hole.get("a") or hole.get("start"))
            hp2 = get_point(hole.get("p2") or hole.get("b") or hole.get("end"))

            if not hp1 or not hp2:
                offset = to_float(hole.get("offset"))
                width = to_float(hole.get("width") or hole.get("length"))

                if offset is not None and width is not None:
                    total_len = line_length(p1, p2)
                    if total_len > 0:
                        start_dist = max(0, offset)
                        end_dist = min(total_len, offset + width)
                        hp1 = point_on_segment(p1, p2, start_dist)
                        hp2 = point_on_segment(p1, p2, end_dist)

            if not hp1 or not hp2:
                continue

            group = str(hole.get("group") or hole.get("kind") or hole.get("category") or "").lower()
            htype = str(hole.get("type") or hole.get("name") or "").lower()

            holes.append({
                "p1": hp1,
                "p2": hp2,
                "group": group,
                "type": htype,
            })

        walls.append({
            "p1": p1,
            "p2": p2,
            "depth": depth,
            "holes": holes,
        })

    return walls


def draw_wall_dimension(ax, p1, p2, offset=22, fontsize=7):
    length = line_length(p1, p2)
    if length <= 0:
        return

    nx, ny = perpendicular_vector(p1, p2)

    mp = line_midpoint(p1, p2)
    tp = offset_point(mp, nx * offset, ny * offset)

    angle = math.degrees(math.atan2(p2["y"] - p1["y"], p2["x"] - p1["x"]))
    if angle > 90 or angle < -90:
        angle += 180

    draw_text(ax, tp["x"], tp["y"], f"{int(round(length))}", fontsize=fontsize, rotation=angle)


def draw_door_symbol(ax, wall_p1, wall_p2, hole_p1, hole_p2, wall_lw):
    dx = wall_p2["x"] - wall_p1["x"]
    dy = wall_p2["y"] - wall_p1["y"]
    wall_angle = math.atan2(dy, dx)

    door_width = line_length(hole_p1, hole_p2)
    if door_width <= 0:
        return

    hinge = hole_p1

    leaf_angle = wall_angle + math.radians(45)
    leaf_end = {
        "x": hinge["x"] + door_width * math.cos(leaf_angle),
        "y": hinge["y"] + door_width * math.sin(leaf_angle),
    }

    draw_line(
        ax,
        hinge,
        leaf_end,
        color="black",
        lw=max(1.0, wall_lw * 0.45),
        zorder=5,
    )

    draw_arc(
        ax,
        center=hinge,
        radius=door_width,
        start_angle=wall_angle,
        end_angle=leaf_angle,
        steps=30,
        color="gray",
        lw=0.8,
    )


def draw_window_symbol(ax, p1, p2):
    dx = p2["x"] - p1["x"]
    dy = p2["y"] - p1["y"]
    length = math.hypot(dx, dy)

    if length == 0:
        return

    ux = dx / length
    uy = dy / length
    offset = 3

    draw_line(ax, p1, p2, color="dimgray", lw=1.2, zorder=5)

    ax.plot(
        [p1["x"] - uy * offset, p2["x"] - uy * offset],
        [p1["y"] + ux * offset, p2["y"] + ux * offset],
        color="dimgray",
        linewidth=0.8,
        zorder=5,
    )


def draw_wall(ax, wall):
    p1 = wall["p1"]
    p2 = wall["p2"]
    depth = wall["depth"]
    holes = wall["holes"]

    lw = max(1.2, depth / 10)

    if not holes:
        draw_line(ax, p1, p2, color="black", lw=lw, zorder=2)
        return

    total_len = line_length(p1, p2)
    if total_len <= 0:
        return

    ux = (p2["x"] - p1["x"]) / total_len
    uy = (p2["y"] - p1["y"]) / total_len

    def proj_len(pt):
        return (pt["x"] - p1["x"]) * ux + (pt["y"] - p1["y"]) * uy

    holes_sorted = sorted(
        holes,
        key=lambda h: min(proj_len(h["p1"]), proj_len(h["p2"]))
    )

    current = p1

    for hole in holes_sorted:
        hp1 = hole["p1"]
        hp2 = hole["p2"]

        if proj_len(hp1) > proj_len(hp2):
            hp1, hp2 = hp2, hp1

        draw_line(ax, current, hp1, color="black", lw=lw, zorder=2)

        group = hole["group"]
        htype = hole["type"]

        is_door = (
            "door" in group or "door" in htype or
            "двер" in group or "двер" in htype
        )

        is_window = (
            "window" in group or "window" in htype or
            "окн" in group or "окн" in htype
        )

        if is_door:
            draw_door_symbol(ax, p1, p2, hp1, hp2, lw)
        elif is_window:
            draw_window_symbol(ax, hp1, hp2)
        else:
            draw_line(ax, hp1, hp2, color="gray", lw=1.0, zorder=3)

        current = hp2

    draw_line(ax, current, p2, color="black", lw=lw, zorder=2)


def render_plan_to_pdf(input_file, output_file):
    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.exists():
        messagebox.showerror("Ошибка", f"Файл не найден:\n{input_path}")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    plan = data.get("plan", data)

    walls = collect_walls(plan)
    rooms = collect_rooms(plan)

    if not walls:
        messagebox.showerror("Ошибка", "Не удалось найти стены в файле.")
        return

    xs = []
    ys = []

    for wall in walls:
        xs.extend([wall["p1"]["x"], wall["p2"]["x"]])
        ys.extend([wall["p1"]["y"], wall["p2"]["y"]])

        for hole in wall["holes"]:
            xs.extend([hole["p1"]["x"], hole["p2"]["x"]])
            ys.extend([hole["p1"]["y"], hole["p2"]["y"]])

    for room in rooms:
        if room["center"]:
            xs.append(room["center"]["x"])
            ys.append(room["center"]["y"])
        for p in room["polygon"]:
            xs.append(p["x"])
            ys.append(p["y"])

    if not xs or not ys:
        messagebox.showerror("Ошибка", "Не удалось извлечь координаты плана.")
        return

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    width = max_x - min_x
    height = max_y - min_y

    if width <= 0 or height <= 0:
        messagebox.showerror("Ошибка", "Некорректные размеры плана.")
        return

    fig_w = 16
    fig_h = max(6, fig_w * (height / width))

    plt.figure(figsize=(fig_w, fig_h))
    ax = plt.gca()

    for wall in walls:
        draw_wall(ax, wall)

    for wall in walls:
        draw_wall_dimension(ax, wall["p1"], wall["p2"], offset=14, fontsize=6)

    for room in rooms:
        center = room["center"]
        area = room["area"]

        if center and area is not None:
            text = f"S={area:.2f} м²"
            if room["name"]:
                text = f"{room['name']}\n{text}"
            draw_text(ax, center["x"], center["y"], text, fontsize=3.5)

    margin = max(width, height) * 0.04
    ax.set_xlim(min_x - margin, max_x + margin)
    ax.set_ylim(max_y + margin, min_y - margin)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

    plt.savefig(output_path, format="pdf", bbox_inches="tight", pad_inches=0.15)
    plt.close()

    messagebox.showinfo("Готово", f"PDF сохранён:\n{output_path}")


def main():
    root = tk.Tk()
    root.withdraw()

    input_file = filedialog.askopenfilename(
        title="Выберите файл .plan",
        filetypes=[("Plan files", "*.plan"), ("JSON files", "*.json"), ("All files", "*.*")]
    )

    if not input_file:
        return

    output_file = filedialog.asksaveasfilename(
        title="Сохранить PDF как",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )

    if not output_file:
        return

    try:
        render_plan_to_pdf(input_file, output_file)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка:\n{e}")


if __name__ == "__main__":
    main()