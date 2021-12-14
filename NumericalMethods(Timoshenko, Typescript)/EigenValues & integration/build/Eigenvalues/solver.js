"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.solver = void 0;
var eps = Math.pow(10, -3);
var printMatrix3x3 = function (matrix) {
    console.log('_______________');
    for (var i = 0; i < 3; i++) {
        for (var j = 0; j < 3; j++) {
            process.stdout.write((matrix[i][j].toFixed(2)).padEnd(10));
        }
        console.log();
    }
};
var solver = function () {
    var A = [
        [2, 1, 0],
        [1, 2, 1],
        [0, 1, 2]
    ];
    var maxA = matrixNorm(A);
    console.log('matrix norm:', maxA);
    var B = [[], [], []];
    for (var i = 0; i < 3; i++) {
        for (var j = 0; j < 3; j++) {
            if (i == j) {
                B[i][j] = maxA - A[i][j];
            }
            else {
                B[i][j] = (-1) * A[i][j];
            }
        }
    }
    console.log('B matrix:');
    printMatrix3x3(B);
    var maxB = maxEigen(B);
    console.log("_____________-");
    return maxA - maxB;
};
exports.solver = solver;
var matrixNorm = function (A) {
    var max = -1;
    for (var i = 0; i < 3; i++) {
        var cur = 0;
        for (var j = 0; j < 3; j++) {
            cur += Math.abs(A[i][j]);
        }
        if (max < cur)
            max = cur;
    }
    return max;
};
var maxEigen = function (A) {
    var currX = [-1, -1, 0];
    var prevX = [0, 0, 0];
    var currMu = 0;
    var prevMu = 0;
    do {
        console.log('__________-');
        var norm = vectorNorm(currX);
        console.log('vector norm:', norm);
        for (var i = 0; i < 3; i++) {
            prevX[i] = currX[i] / norm;
        }
        console.log('normalized vector', prevX);
        currX = multiplyMatrixByVector(A, prevX);
        console.log('vector after multiplying by current matrix', currX);
        prevMu = currMu;
        currMu = dotProduct(prevX, currX);
        console.log('currnet approximation:', currMu);
    } while (Math.abs(currMu - prevMu) > eps);
    return currMu;
};
var dotProduct = function (x, y) {
    var res = 0;
    for (var i = 0; i < 3; i++) {
        res += x[i] * y[i];
    }
    return res;
};
var vectorNorm = function (x) {
    var res = 0;
    for (var i = 0; i < 3; i++) {
        res += x[i] * x[i];
    }
    return Math.sqrt(res);
};
var multiplyMatrixByVector = function (matrix, vector) {
    var newVector = new Array(3).fill(0);
    for (var i = 0; i < 3; i++) {
        for (var j = 0; j < 3; j++) {
            newVector[i] += matrix[i][j] * vector[j];
        }
    }
    return newVector;
};
