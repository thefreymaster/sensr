var express = require('express');
var sense = require("node-sense-hat")
//All Sense Hat Constants
const JoystickLib = sense.Joystick;

const app = express()

const colors = require('./constants/colors');
const directions = require('./constants/directions');
const numbers = require('./constants/letters');

app.use(express.json());

let digitOne = "";
let digitTwo = "";

const port = 9700;
var server = app.listen(process.env.PORT || port, function () {
    console.log('Running Express server on port: ' + port);
});

JoystickLib.getJoystick().then(joystick => {
    console.log(joystick);
});

const determineEnglishDigit = (number, digit) => {
    let num = number.toString();
    switch (num[digit]) {
        case '0':
            return numbers.zero;
        case '1':
            return numbers.one;
        case '2':
            return numbers.two;
        case '3':
            return numbers.three;
        case '4':
            return numbers.four;
        case '5':
            return numbers.five;
        case '6':
            return numbers.six;
        case '7':
            return numbers.seven;
        case '8':
            return numbers.eight;
        case '9':
            return numbers.nine;

    }
}

const combineDigitArrays = (digitOneArray, digitTwoArray, OnColor, OffColor) => {
    let i = 0;
    let j = 0;
    for (i; i < digitOneArray.length; i++) {
        if (digitOneArray[i] == 0)
            ledArray.append(OffColor)
        if (digitOneArray[i] == 1)
            ledArray.append(OnColor)
        if ((i + 1) % 4 === 0) {
            for (j; j < digitTwoArray.length; j++) {
                if (digitTwoArray[j] === 0)
                    ledArray.append(OffColor)
                if (digitTwoArray[j] === 1)
                    ledArray.append(OnColor)
            }
        }
    }
    return ledArray;
}

const translateDirectionToColors = (direction, OnColor, OffColor) => {
    p = 0
    for (p; p < digitOneArray.length; p++) {
        if (direction[p] == 0)
            ledArray.append(OffColor)
        if (direction[p] == 1)
            ledArray.append(OnColor)
    }
    return ledArray
}

const convertTemp = (temp) => {
    let tempF = (temp * (9 / 5) + 32);
    if (tempF >= 100)
        return 99;
    return tempF;
}

const convertPressureToPercent = (pressure) => {
    press = (pressure / 1080) * 100;
    return press;
}


app.get('/api/status', (req, res) => {
    res.send({
        system: true,
        version: '1.00.0',
        app: 'Lights',
        colors: colors
    })
})