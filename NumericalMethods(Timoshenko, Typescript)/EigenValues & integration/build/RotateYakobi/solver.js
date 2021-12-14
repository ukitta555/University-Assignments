"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.solver = void 0;
var transposeMatrix = function (matrix) {
    var transposedMatrix = [[], [], []];
    for (var i = 0; i < 3; i++) {
        transposedMatrix[i] = [0, 0, 0];
    }
    for (var i = 0; i < 3; i++) {
        for (var j = 0; j < 3; j++) {
            transposedMatrix[j][i] = matrix[i][j];
        }
    }
    return transposedMatrix;
};
var printMatrix3x3 = function (matrix) {
    console.log('_______________');
    for (var i = 0; i < 3; i++) {
        for (var j = 0; j < 3; j++) {
            process.stdout.write((matrix[i][j].toFixed(2)).padEnd(10));
        }
        console.log();
    }
};
var multiplyMatrices = function (firstMatrix, secondMatrix) {
    var resultMatrix = [[], [], []];
    for (var i = 0; i < 3; i++) {
        resultMatrix[i] = [0, 0, 0];
    }
    for (var i = 0; i < 3; i++) {
        for (var j = 0; j < 3; j++) {
            //console.log(`indices for result matrix: ${i}, ${j}`)
            //console.log('_______________________')
            for (var k = 0; k < 3; k++) {
                resultMatrix[i][j] += firstMatrix[i][k] * secondMatrix[k][j];
                //console.log(`first matrix element: ${firstMatrix[i][k]}, second matrix element: ${secondMatrix[k][j]}`)
                /*printMatrix(resultMatrix)*/
            }
        }
    }
    return resultMatrix;
};
var solver = function () {
    var A = [
        [3, 2, 1],
        [2, 1, 1],
        [1, 1, 3]
    ];
    console.log('t(a)', square(A));
    for (var q = 0; q < 3; q++) {
        var _a = findMax(A), iMax = _a[0], jMax = _a[1], max = _a[2];
        console.log("max, i, j: " + max + ", " + (iMax + 1) + ", " + (jMax + 1));
        var tgTwoPhi = (A[iMax][iMax] - A[jMax][jMax])
            ? (2 * max) / (A[iMax][iMax] - A[jMax][jMax])
            : Math.PI / 4;
        console.log("tg2phi: " + tgTwoPhi);
        var phi = Math.abs(Math.atan(tgTwoPhi) / 2);
        console.log('phi', phi);
        var cosPhi = Math.cos(phi);
        var sinPhi = Math.sin(phi);
        console.log("cosphi, sinphi: " + cosPhi + ", " + sinPhi);
        var U = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ];
        for (var i = 0; i < 3; i++) {
            for (var j = 0; j < 3; j++) {
                U[i][j] = 0;
                if (i === j) {
                    U[i][j] = 1;
                }
            }
        }
        U[iMax][iMax] = cosPhi;
        U[iMax][jMax] = sinPhi;
        U[jMax][iMax] = -sinPhi;
        U[jMax][jMax] = cosPhi;
        console.log('U matrix:');
        printMatrix3x3(U);
        var U_T = transposeMatrix(U);
        console.log('U_T:');
        printMatrix3x3(U_T);
        var an = multiplyMatrices(U, A);
        printMatrix3x3(an);
        var ANext = multiplyMatrices(an, U_T);
        console.log('A_Next:');
        printMatrix3x3(ANext);
        A = ANext;
        console.log('t(a)', square(A));
    }
};
exports.solver = solver;
var findMax = function (A) {
    var iMax = 0, jMax = 0, max = -10000;
    for (var i = 0; i < 3; i++) {
        for (var j = 0; j < 3; j++) {
            if (i !== j && max < Math.abs(A[i][j])) {
                iMax = i;
                jMax = j;
                max = Math.abs(A[i][j]);
            }
        }
    }
    return [iMax, jMax, max];
};
var square = function (A) {
    var sum = 0;
    for (var i = 0; i < 3; i++) {
        for (var j = 0; j < 3; j++) {
            if (i !== j) {
                sum += Math.pow(A[i][j], 2);
            }
        }
    }
    return sum;
};
