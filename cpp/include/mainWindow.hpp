#pragma once

#include <QMainWindow>
#include <QTabWidget>
#include <QGraphicsView>
#include <QPlainTextEdit>
#include <QSpinBox>
#include <QPushButton>
#include <opencv2/core/mat.hpp>

class MainWindow : public QMainWindow {
    Q_OBJECT

public:
    explicit MainWindow(QWidget* parent = nullptr);

private slots:
    void selectCoverImage();
    void handleCoverImageSelected(const cv::Mat& image);
    void hideMessage();
    void saveStegoImage();
    void selectStegoImage();
    void decodeMessage();

private:
    void setupUi();
    void displayImage(const cv::Mat& image, QGraphicsView* view);

    QTabWidget* tabWidget;
    
    // Encoder widgets
    QGraphicsView* coverGraphicsView;
    QGraphicsView* stegoGraphicsView;
    QPlainTextEdit* encoderPlainTextEdit;
    QSpinBox* encoderBitSpinBox;
    QPushButton* selectCoverButton;
    QPushButton* hideButton;
    QPushButton* saveStegoButton;

    // Decoder widgets
    QGraphicsView* decoderGraphView;
    QPlainTextEdit* decoderPlainTextEdit;
    QSpinBox* decoderBitSpinBox;
    QPushButton* selectStegoButton;
    QPushButton* decodeButton;

    cv::Mat coverImage;
    cv::Mat stegoImage;
}; 