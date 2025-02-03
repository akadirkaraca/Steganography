import math


class Prestige:
    class State:
        HIDING = 0
        SOLVING = 1
        EOT = 2 # End of Text

    @staticmethod
    def encode(secretText, coverImage, changeBitValue):
        """
        secretText: 
        coverImage: 
        changeBitValue: 
        
        return: PIL.Image
        """
        state = Prestige.State.HIDING
        charIndex = 0
        charValue = 0
        newCharControl = 0
        changeBit = changeBitValue
        power = int(math.pow(2, changeBit))

        secretText += '\0'

        width, height = coverImage.size
        pixels = coverImage.load()

        for i in range(height):
            if state == Prestige.State.EOT:
                break
            for j in range(width):
                if state == Prestige.State.EOT:
                    break

                pixel = pixels[j, i]
                R = pixel[0] - (pixel[0] % power)
                G = pixel[1] - (pixel[1] % power)
                B = pixel[2] - (pixel[2] % power)

                for n in range(3):
                    if newCharControl == 0 or newCharControl > 8:
                        if charIndex >= len(secretText):
                            state = Prestige.State.EOT
                        else:
                            charValue = ord(secretText[charIndex])
                            charIndex += 1
                            newCharControl = 0

                    if state == Prestige.State.HIDING:
                        if n == 0:
                            R += charValue % power
                            charValue //= power
                        elif n == 1:
                            G += charValue % power
                            charValue //= power
                        elif n == 2:
                            B += charValue % power
                            charValue //= power
                            pixels[j, i] = (R, G, B)

                    newCharControl += changeBit

        return coverImage

    @staticmethod
    def decode(stegoImage, changedBit):
        """
        stegoImage: 
        changedBit: 
        
        return: 
        """
        state = Prestige.State.SOLVING

        hiddenText = ""
        hiddenCharValue = 0
        currentIterationCount = 0

        iterationCountPerChar = [0, 8, 4, 2, 2, 1, 1, 1, 1]
        maskForGetLsbValue = [0, 1, 3, 7, 15, 31, 63, 127, 255]

        binaryChangedBitDecimalValue = int(math.pow(2, changedBit))

        width, height = stegoImage.size
        pixels = stegoImage.load()

        for i in range(height):
            if state == Prestige.State.EOT:
                break
            for j in range(width):
                if state == Prestige.State.EOT:
                    break

                pixel = pixels[j, i]
                R = pixel[0] & maskForGetLsbValue[changedBit]
                G = pixel[1] & maskForGetLsbValue[changedBit]
                B = pixel[2] & maskForGetLsbValue[changedBit]

                for n in range(3):
                    if currentIterationCount > iterationCountPerChar[changedBit]:
                        hiddenChar = chr(hiddenCharValue)
                        if hiddenChar == '\0':
                            state = Prestige.State.EOT
                            break
                        else:
                            hiddenText += hiddenChar
                        hiddenCharValue = 0
                        currentIterationCount = 0

                    if state == Prestige.State.SOLVING:
                        if n == 0:
                            hiddenCharValue += R * (binaryChangedBitDecimalValue ** currentIterationCount)
                            currentIterationCount += 1
                        elif n == 1:
                            hiddenCharValue += G * (binaryChangedBitDecimalValue ** currentIterationCount)
                            currentIterationCount += 1
                        elif n == 2:
                            hiddenCharValue += B * (binaryChangedBitDecimalValue ** currentIterationCount)
                            currentIterationCount += 1

                if state == Prestige.State.EOT:
                    break

        return hiddenText
