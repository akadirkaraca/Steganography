#include <cmath>
#include "prestige.hpp"

const std::array<int, 9> Prestige::iterationCountPerChar = {0, 8, 4, 2, 2, 1, 1, 1, 1};
const std::array<int, 9> Prestige::maskForGetLsbValue = {0, 1, 3, 7, 15, 31, 63, 127, 255};

cv::Mat Prestige::encode(const std::string& secretText, const cv::Mat& coverImage, int changeBitValue) {
    State state = State::HIDING;
    size_t charIndex = 0;
    int charValue = 0;
    int newCharControl = 0;
    int power = static_cast<int>(std::pow(2, changeBitValue));

    cv::Mat stegoImage = coverImage.clone();
    std::string text = secretText + '\0';

    for (int i = 0; i < stegoImage.rows && state != State::EOT; ++i) {
        for (int j = 0; j < stegoImage.cols && state != State::EOT; ++j) {
            cv::Vec3b& pixel = stegoImage.at<cv::Vec3b>(i, j);
            
            int R = pixel[2] - (pixel[2] % power);
            int G = pixel[1] - (pixel[1] % power);
            int B = pixel[0] - (pixel[0] % power);

            for (int n = 0; n < 3; ++n) {
                if (newCharControl == 0 || newCharControl > 8) {
                    if (charIndex >= text.length()) {
                        state = State::EOT;
                    } else {
                        charValue = static_cast<int>(text[charIndex]);
                        charIndex++;
                        newCharControl = 0;
                    }
                }

                if (state == State::HIDING) {
                    switch (n) {
                        case 0:
                            R += charValue % power;
                            charValue /= power;
                            break;
                        case 1:
                            G += charValue % power;
                            charValue /= power;
                            break;
                        case 2:
                            B += charValue % power;
                            charValue /= power;
                            pixel = cv::Vec3b(B, G, R);
                            break;
                    }
                }
                newCharControl += changeBitValue;
            }
        }
    }
    return stegoImage;
}

std::string Prestige::decode(const cv::Mat& stegoImage, int changedBit) {
    State state = State::SOLVING;
    std::string hiddenText;
    int hiddenCharValue = 0;
    int currentIterationCount = 0;
    int binaryChangedBitDecimalValue = static_cast<int>(std::pow(2, changedBit));

    for (int i = 0; i < stegoImage.rows && state != State::EOT; ++i) {
        for (int j = 0; j < stegoImage.cols && state != State::EOT; ++j) {
            const cv::Vec3b& pixel = stegoImage.at<cv::Vec3b>(i, j);
            
            int R = pixel[2] & maskForGetLsbValue[changedBit];
            int G = pixel[1] & maskForGetLsbValue[changedBit];
            int B = pixel[0] & maskForGetLsbValue[changedBit];

            for (int n = 0; n < 3; ++n) {
                if (currentIterationCount > iterationCountPerChar[changedBit]) {
                    char hiddenChar = static_cast<char>(hiddenCharValue);
                    if (hiddenChar == '\0') {
                        state = State::EOT;
                        break;
                    }
                    hiddenText += hiddenChar;
                    hiddenCharValue = 0;
                    currentIterationCount = 0;
                }

                if (state == State::SOLVING) {
                    switch (n) {
                        case 0:
                            hiddenCharValue += R * static_cast<int>(std::pow(binaryChangedBitDecimalValue, currentIterationCount));
                            currentIterationCount++;
                            break;
                        case 1:
                            hiddenCharValue += G * static_cast<int>(std::pow(binaryChangedBitDecimalValue, currentIterationCount));
                            currentIterationCount++;
                            break;
                        case 2:
                            hiddenCharValue += B * static_cast<int>(std::pow(binaryChangedBitDecimalValue, currentIterationCount));
                            currentIterationCount++;
                            break;
                    }
                }
            }
        }
    }
    return hiddenText;
} 