#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QFileDialog>
#include <QGraphicsScene>
#include <QImage>
#include <QPixmap>
#include <QDebug>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include "mainWindow.hpp"
#include "prestige.hpp"


MainWindow::MainWindow(QWidget* parent)
    : QMainWindow(parent)
{
    setupUi();
    setWindowTitle("Steganography LSB");
    setMinimumSize(1024, 680);
}

void MainWindow::setupUi() {
    QWidget* centralWidget = new QWidget(this);
    setCentralWidget(centralWidget);
    
    QHBoxLayout* mainLayout = new QHBoxLayout(centralWidget);
    mainLayout->setObjectName("horizontalLayout_3");
    
    tabWidget = new QTabWidget(centralWidget);
    tabWidget->setEnabled(true);
    tabWidget->setTabShape(QTabWidget::Triangular);
    
    QWidget* encoderTab = new QWidget();
    QGridLayout* gridLayout_2 = new QGridLayout(encoderTab);
    
    QVBoxLayout* encoderLayout = new QVBoxLayout();
    encoderLayout->setSizeConstraint(QLayout::SetDefaultConstraint);
    
    QHBoxLayout* encoderGraphLayout = new QHBoxLayout();
    
    QVBoxLayout* coverLayout = new QVBoxLayout();
    coverGraphicsView = new QGraphicsView(encoderTab);
    QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
    coverGraphicsView->setSizePolicy(sizePolicy);
    coverLayout->addWidget(coverGraphicsView);
    
    selectCoverButton = new QPushButton(encoderTab);
    selectCoverButton->setText(tr("Select Cover"));
    selectCoverButton->setIcon(QIcon::fromTheme("camera-photo"));
    connect(selectCoverButton, &QPushButton::clicked, this, &MainWindow::selectCoverImage);
    coverLayout->addWidget(selectCoverButton);
    
    encoderGraphLayout->addLayout(coverLayout);
    
    QVBoxLayout* stegoLayout = new QVBoxLayout();
    stegoGraphicsView = new QGraphicsView(encoderTab);
    stegoGraphicsView->setSizePolicy(sizePolicy);
    stegoLayout->addWidget(stegoGraphicsView);
    
    saveStegoButton = new QPushButton(encoderTab);
    saveStegoButton->setText(tr("Save Stego"));
    QSizePolicy buttonSizePolicy(QSizePolicy::Minimum, QSizePolicy::Preferred);
    saveStegoButton->setSizePolicy(buttonSizePolicy);
    saveStegoButton->setIcon(QIcon::fromTheme("document-save"));
    connect(saveStegoButton, &QPushButton::clicked, this, &MainWindow::saveStegoImage);
    stegoLayout->addWidget(saveStegoButton);
    
    encoderGraphLayout->addLayout(stegoLayout);
    encoderLayout->addLayout(encoderGraphLayout);
    
    QVBoxLayout* encoderConfigLayout = new QVBoxLayout();
    
    QHBoxLayout* textEditLayout = new QHBoxLayout();
    encoderPlainTextEdit = new QPlainTextEdit(encoderTab);
    encoderPlainTextEdit->setPlaceholderText(tr("Please type text that will be hidden"));
    textEditLayout->addWidget(encoderPlainTextEdit);
    encoderConfigLayout->addLayout(textEditLayout);
    
    QHBoxLayout* encoderRunLayout = new QHBoxLayout();
    
    QLabel* encoderBitLabel = new QLabel(tr("Bit Count"), encoderTab);
    QSizePolicy labelSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    labelSizePolicy.setHorizontalStretch(1);
    encoderBitLabel->setSizePolicy(labelSizePolicy);
    encoderRunLayout->addWidget(encoderBitLabel);
    
    encoderBitSpinBox = new QSpinBox(encoderTab);
    QSizePolicy spinBoxSizePolicy(QSizePolicy::Minimum, QSizePolicy::Fixed);
    spinBoxSizePolicy.setHorizontalStretch(3);
    encoderBitSpinBox->setSizePolicy(spinBoxSizePolicy);
    encoderBitSpinBox->setRange(1, 8);
    encoderBitSpinBox->setValue(1);
    encoderRunLayout->addWidget(encoderBitSpinBox);
    
    hideButton = new QPushButton(tr("Hide"), encoderTab);
    hideButton->setSizePolicy(spinBoxSizePolicy);
    connect(hideButton, &QPushButton::clicked, this, &MainWindow::hideMessage);
    encoderRunLayout->addWidget(hideButton);
    
    encoderConfigLayout->addLayout(encoderRunLayout);
    encoderLayout->addLayout(encoderConfigLayout);
    
    gridLayout_2->addLayout(encoderLayout, 0, 0);
    
    QWidget* decoderTab = new QWidget();
    QGridLayout* gridLayout_3 = new QGridLayout(decoderTab);
    
    QVBoxLayout* decoderLayout = new QVBoxLayout();
    
    QVBoxLayout* decoderGraphLayout = new QVBoxLayout();
    decoderGraphView = new QGraphicsView(decoderTab);
    decoderGraphLayout->addWidget(decoderGraphView);
    
    selectStegoButton = new QPushButton(tr("Select Stego"), decoderTab);
    selectStegoButton->setIcon(QIcon::fromTheme("camera-photo"));
    connect(selectStegoButton, &QPushButton::clicked, this, &MainWindow::selectStegoImage);
    decoderGraphLayout->addWidget(selectStegoButton);
    
    decoderLayout->addLayout(decoderGraphLayout);
    
    QVBoxLayout* decoderConfigLayout = new QVBoxLayout();
    
    QHBoxLayout* horizontalLayout = new QHBoxLayout();
    decoderPlainTextEdit = new QPlainTextEdit(decoderTab);
    horizontalLayout->addWidget(decoderPlainTextEdit);
    decoderConfigLayout->addLayout(horizontalLayout);
    
    QHBoxLayout* decoderRunLayout = new QHBoxLayout();
    
    QLabel* decoderBitLabel = new QLabel(tr("Bit Count"), decoderTab);
    decoderBitLabel->setSizePolicy(labelSizePolicy);
    decoderRunLayout->addWidget(decoderBitLabel);
    
    decoderBitSpinBox = new QSpinBox(decoderTab);
    decoderBitSpinBox->setSizePolicy(spinBoxSizePolicy);
    decoderBitSpinBox->setRange(1, 8);
    decoderBitSpinBox->setValue(1);
    decoderRunLayout->addWidget(decoderBitSpinBox);
    
    decodeButton = new QPushButton(tr("Decode"), decoderTab);
    decodeButton->setSizePolicy(spinBoxSizePolicy);
    connect(decodeButton, &QPushButton::clicked, this, &MainWindow::decodeMessage);
    decoderRunLayout->addWidget(decodeButton);
    
    decoderConfigLayout->addLayout(decoderRunLayout);
    decoderLayout->addLayout(decoderConfigLayout);
    
    gridLayout_3->addLayout(decoderLayout, 0, 0);
    
    tabWidget->addTab(encoderTab, tr("Encoder"));
    tabWidget->addTab(decoderTab, tr("Decoder"));
    
    mainLayout->addWidget(tabWidget);
    
    tabWidget->setCurrentIndex(0);
}

void MainWindow::displayImage(const cv::Mat& image, QGraphicsView* view) {
    cv::Mat rgb;
    if (image.channels() == 3) {
        cv::cvtColor(image, rgb, cv::COLOR_BGR2RGB);
    } else {
        rgb = image;
    }

    QImage qimage(rgb.data, rgb.cols, rgb.rows, rgb.step, QImage::Format_RGB888);
    QPixmap pixmap = QPixmap::fromImage(qimage);

    QGraphicsScene* scene = new QGraphicsScene();
    scene->addPixmap(pixmap);
    view->setScene(scene);
    view->fitInView(scene->itemsBoundingRect(), Qt::KeepAspectRatio);
}

void MainWindow::handleCoverImageSelected(const cv::Mat& image) {
    coverImage = image;
    displayImage(coverImage, coverGraphicsView);
}

void MainWindow::saveStegoImage() {
    if (stegoImage.empty()) {
        qDebug() << "Please compose stego image by hiding process";
        return;
    }

    QString fileName = QFileDialog::getSaveFileName(this,
        tr("Save Stego Image"), "",
        tr("PNG Files (*.png);;JPEG Files (*.jpg *.jpeg);;BMP Files (*.bmp)"));

    if (!fileName.isEmpty()) {
        try {
            cv::imwrite(fileName.toStdString(), stegoImage);
            qDebug() << "Image saved:" << fileName;
        } catch (const cv::Exception& e) {
            qDebug() << "Image cannot be saved:" << e.what();
        }
    }
}

void MainWindow::selectStegoImage() {
    QString fileName = QFileDialog::getOpenFileName(this,
        tr("Select Stego Image"), "",
        tr("Image Files (*.png *.jpg *.jpeg *.bmp)"));

    if (!fileName.isEmpty()) {
        stegoImage = cv::imread(fileName.toStdString());
        if (!stegoImage.empty()) {
            displayImage(stegoImage, decoderGraphView);
        }
    }
}

void MainWindow::decodeMessage() {
    if (stegoImage.empty()) {
        qDebug() << "Please select stego image";
        return;
    }

    int bitValue = decoderBitSpinBox->value();
    std::string decodedMessage = Prestige::decode(stegoImage, bitValue);
    decoderPlainTextEdit->setPlainText(QString::fromStdString(decodedMessage));
}

void MainWindow::selectCoverImage() {
    QString fileName = QFileDialog::getOpenFileName(this,
        tr("Select Cover Image"), "",
        tr("Image Files (*.png *.jpg *.jpeg *.bmp)"));
        
    if (!fileName.isEmpty()) {
        coverImage = cv::imread(fileName.toStdString());
        if (!coverImage.empty()) {
            displayImage(coverImage, coverGraphicsView);
        }
    }
}

void MainWindow::hideMessage() {
    if (coverImage.empty()) {
        qDebug() << "Please select cover image first";
        return;
    }

    std::string secretText = encoderPlainTextEdit->toPlainText().toStdString();
    if (secretText.empty()) {
        qDebug() << "Please enter text to hide";
        return;
    }

    int bitValue = encoderBitSpinBox->value();
    stegoImage = Prestige::encode(secretText, coverImage, bitValue);
    
    if (!stegoImage.empty()) {
        displayImage(stegoImage, stegoGraphicsView);
    } else {
        qDebug() << "Failed to create stego image";
    }
}