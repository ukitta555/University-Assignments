"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.run = exports.f = void 0;
var f = function (x) { return x * x * x * x * x + 2 * (Math.pow(x, 4)) + 3 * (Math.pow(x, 2)); };
exports.f = f;
var eps = Math.pow(10, -3);
var run = function (a, b) {
    var nByTwo = 2;
    // let prevCalc = calculateForN(nByTwo, a, b)
    //  let currCalc = calculateForN(nByTwo *= 2, a, b)
    console.log(calculateForN(4, a, b));
    // Runge's rule
    //  while ((1/15) * Math.abs(currCalc - prevCalc) > eps) {
    //   prevCalc = currCalc
    //    currCalc = calculateForN(nByTwo *= 2, a, b)
    //  }
    //  return currCalc
};
exports.run = run;
var calculateForN = function (nByTwo, a, b) {
    var result = 0;
    var h = (b - a) / nByTwo;
    var vertices = [];
    var currentStep = a;
    while (currentStep <= b) {
        vertices.push(currentStep);
        currentStep += h;
    }
    console.log("adding f(first vertex) and f(last vertex): " + exports.f(vertices[0]) + ", " + exports.f(vertices[vertices.length - 1]));
    result = exports.f(vertices[0]) + exports.f(vertices[vertices.length - 1]);
    console.log('result', result);
    for (var i = 1; i < vertices.length - 1; i++) {
        if (i % 2 === 0) {
            console.log("adding f(vertex " + i + ") by 2: " + exports.f(vertices[i]) * 2);
            result += exports.f(vertices[i]) * 2;
            console.log('result', result);
        }
        else {
            console.log("adding f(vertex " + i + ") by 4: " + exports.f(vertices[i]) * 4);
            result += exports.f(vertices[i]) * 4;
            console.log('result', result);
        }
    }
    console.log('step length', h);
    console.log('returning result * step /3', result * h / 3);
    return result * h / 3;
};
