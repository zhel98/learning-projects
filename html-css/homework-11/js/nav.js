// В результате действия данного скрипта,
// по клику на кнопку с id="navBtn"
// элемент с id="navBlock" будет плавно,  появляться, если он скрыт
//  и скрываться, если он виден.

// Для того, чтобы этот скрипт работал корректно,
// у элемента с id="navBlock" (в вашей верстке это будет элемент div или nav в который завернут список с пунктами навигации)
// изначально должен быть класс block-hidden и тогда когда этот блок будет скрыт у него должно быть свойство height: 0:
// .block-hidden {
//   height: 0;
// }

// также у блока c навигацией обязательно должны быть свойства:
// .класс-блока-с-навигацией {
//   overflow: hidden;
//   transition: height 1s;
//  }

// чтобы высота блока навигации соответствовала высоте элемента ul находящегося в нем, у элемента ul обязательно должны быть обнулены вертикальные маржины

// точка перехода блока навигации в скрытое || развернутое состояние в данном проекте 1200px, 
// если блок навигации должен скрываться || показываться  при другой ширине экрана, нужно изменить значение переменной point


function navToggle() {

	const navBtn = document.getElementById('navBtn');
	const navBlock = document.getElementById('navBlock');
	const point = 1260;

	navBtn.onclick = function () {

		let heightNavBlock = navBlock.firstElementChild.offsetHeight;

		if (navBlock.classList.contains('block-hidden')) {

			navBlock.classList.remove('block-hidden');

			navBlock.style.height = heightNavBlock + 'px';

		} else {

			navBlock.classList.add('block-hidden');

			navBlock.style.height = 0;

		}

	}


	window.addEventListener("resize", resizeHandler, false);

	function resizeHandler() {

		let heightNavBlock = navBlock.firstElementChild.offsetHeight;

		if (window.innerWidth >= point) {

			navBlock.style.height = 'auto';

		} else {

			if (navBlock.classList.contains('block-hidden')) {

				navBlock.style.height = 0;

			} else {

				navBlock.style.height = heightNavBlock + 'px';

			}

		}

	}

}

navToggle();
