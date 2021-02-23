
export {createSvgDeleteButton};

function createSvgDeleteButton() {
  let svg = document.createElementNS("http://www.w3.org/2000/svg", 'svg');
  svg.setAttribute("width", "45px");
  svg.setAttribute("height", "45px");
  svg.setAttribute("class", "delete_button");
  let line1 = document.createElementNS("http://www.w3.org/2000/svg", 'line');
  line1.setAttribute('x1', "10");
  line1.setAttribute('y1', "10");
  line1.setAttribute('x2', "40");
  line1.setAttribute('y2', "40");
  line1.setAttribute("stroke", "red");
  line1.setAttribute("stroke-width", '10')
  let line2 = document.createElementNS("http://www.w3.org/2000/svg", 'line');
  line2.setAttribute('x1', "40");
  line2.setAttribute('y1', "10");
  line2.setAttribute('x2', "10");
  line2.setAttribute('y2', "40");
  line2.setAttribute("stroke", "red");
  line2.setAttribute("stroke-width", '10')
  svg.appendChild(line1);
  svg.appendChild(line2);
  return svg;
}
