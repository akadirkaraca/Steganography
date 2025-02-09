#pragma once

#include <string>
#include <opencv2/core/mat.hpp>

class Prestige {
public:
    enum class State {
        HIDING,
        SOLVING,
        EOT  // End of Text
    };

    static cv::Mat encode(const std::string& secretText, const cv::Mat& coverImage, int changeBitValue);
    static std::string decode(const cv::Mat& stegoImage, int changedBit);

private:
    static const int MAX_BIT_VALUE = 8;
    static const std::array<int, 9> iterationCountPerChar;
    static const std::array<int, 9> maskForGetLsbValue;
}; 