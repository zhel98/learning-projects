// В результате действия данного скрипта,
// по клику на кнопку с id="navBtn"
// элемент с id="mainNav" будет плавно,  появляться, если он скрыт
//  и скрываться, если он виден.

// Для того, чтобы этот скрипт работал корректно,
// у элемента с id="mainNav" (в вашей верстке это будет блок навигации)
// изначально должен быть класс nav-hidden
// блок навигации должен скрываться за счет нулевой высоты и свойства 
// overflow - hidden, плавное изменение высоты должны осуществляться при 
// помощи свойства transition

// таким оразом  у блока навигации обязательно должны быть свойства:
// .main-nav {
//   overflow: hidden;
//   transition: height 2s;
//  }
//  и в тот момент когда бллк навигации должен быть скрыт должно 
// появиться свойство height: 0;

// точка перехода блока навигации в скрытое || развернутое состояние в данном проекте 780px, 
// если блок навигации должен скрываться || показываться  при другой ширине экрана, 
// нужно изменить значение переменной point


function navToggle() {

	const navBtn = document.getElementById('navBtn');
	const mainNav = document.getElementById('mainNav');
	const point = 1024;

	navBtn.onclick = function () {

		let heightNav = mainNav.firstElementChild.offsetHeight;

		if (mainNav.classList.contains('nav-hidden')) {

			mainNav.classList.remove('nav-hidden');

			mainNav.style.height = heightNav + 'px';

		} else {

			mainNav.classList.add('nav-hidden');

			mainNav.style.height = 0;

		}

	}


	window.addEventListener("resize", resizeHandler, false);

	function resizeHandler() {

		let heightNav = mainNav.firstElementChild.offsetHeight;

		if (window.innerWidth >= point) {

			mainNav.style.height = 'auto';

		} else {

			if (mainNav.classList.contains('nav-hidden')) {

				mainNav.style.height = 0;

			} else {

				mainNav.style.height = heightNav + 'px';

			}

		}

	}

}

navToggle();