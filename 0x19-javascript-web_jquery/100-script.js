/* window.onload = function () {
  document.querySelector('header').style.color = '#FF0000';
};
Works upon loading the whole webpage */

document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('header').style.color = '#FF0000';
});
/* Works as soon as the page DOM has loaded, without waiting
for resources to finish loading */
