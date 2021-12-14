"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.solver = void 0;
// page 55 1 zh
// page 66 2 a
var eps = Math.pow(10, -3);
var solver = function () {
    var prevX = 0;
    var prevY = 0;
    var prevZ = 0;
    var curX = 1.25;
    var curY = 0;
    var curZ = 0.25;
    do {
        prevX = curX;
        prevY = curY;
        prevZ = curZ;
        curX = Math.sqrt((-(1.5 * prevY * prevY) - (prevZ * prevZ) + 5) / 3);
        curY = (-6 / 5 * prevX * prevY * prevZ) + (1 / 5 * prevX) - (3 / 5 * prevZ);
        curZ = 1 / (5 * prevX - prevY);
        console.log('X', prevX, curX);
        console.log('Y', prevY, curY);
        console.log('Z', prevZ, curZ);
        console.log('___________');
    } while (!compare([prevX, curX], [prevY, curY], [prevZ, curZ]));
    return [curX, curY, curZ];
};
exports.solver = solver;
var compare = function (x, y, z) {
    if (Math.abs(x[0] - x[1]) < eps && Math.abs(y[0] - y[1]) < eps && Math.abs(z[0] - z[1]) < eps)
        return true;
    return false;
};
