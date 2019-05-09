#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QPixmap pix(":/new/prefix1/esse.jpeg");
    int w=ui->label_image_esse->width();
    int h=ui->label_image_esse->height();
    ui->label_image_esse->setPixmap(pix.scaled(w,h,Qt::KeepAspectRatio));

    QPixmap pix2(":/new/prefix1/marlboro.jpeg");
    w=ui->label_image_marlboro->width();
    h=ui->label_image_marlboro->height();
    ui->label_image_marlboro->setPixmap(pix2.scaled(w,h,Qt::KeepAspectRatio));


    QPixmap pix3(":/new/prefix1/bohem_cigar.png");
    w=ui->label_image_bohem->width();
    h=ui->label_image_bohem->height();
    ui->label_image_bohem->setPixmap(pix3.scaled(w,h,Qt::KeepAspectRatio));

    QPixmap pix4(":/new/prefix1/mevius.png");
    w=ui->label_image_mevius->width();
    h=ui->label_image_mevius->height();
    ui->label_image_mevius->setPixmap(pix4.scaled(w,h,Qt::KeepAspectRatio));

    QPixmap pix5(":/new/prefix1/cigar.png");
    w=ui->label_image_logo->width();
    h=ui->label_image_logo->height();
    ui->label_image_logo->setPixmap(pix5.scaled(w,h,Qt::KeepAspectRatio));




}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_1_clicked()
{
    ui->lineEdit_money->setText(ui->lineEdit_money->text()+"1");
}

void MainWindow::on_pushButton_2_clicked()
{
    ui->lineEdit_money->setText(ui->lineEdit_money->text()+"2");
}

void MainWindow::on_pushButton_3_clicked()
{
    ui->lineEdit_money->setText(ui->lineEdit_money->text()+"3");
}

void MainWindow::on_pushButton_4_clicked()
{
    ui->lineEdit_money->setText(ui->lineEdit_money->text()+"4");
}

void MainWindow::on_pushButton_5_clicked()
{
    ui->lineEdit_money->setText(ui->lineEdit_money->text()+"5");
}

void MainWindow::on_pushButton_6_clicked()
{
        ui->lineEdit_money->setText(ui->lineEdit_money->text()+"6");
}

void MainWindow::on_pushButton_7_clicked()
{
        ui->lineEdit_money->setText(ui->lineEdit_money->text()+"7");
}

void MainWindow::on_pushButton_8_clicked()
{
        ui->lineEdit_money->setText(ui->lineEdit_money->text()+"8");
}

void MainWindow::on_pushButton_9_clicked()
{
        ui->lineEdit_money->setText(ui->lineEdit_money->text()+"9");
}

void MainWindow::on_pushButton_0_clicked()
{
        ui->lineEdit_money->setText(ui->lineEdit_money->text()+"0");
}

void MainWindow::on_pushButton_return_clicked()
{
        ui->lineEdit_money->setText("");
}

void MainWindow::on_pushButton_select_esse_clicked()
{
    int money=ui->lineEdit_money->text().toInt();
    if(money>4500)
    {
        money=money-4500;
        QString str=QString::number(money);
        ui->lineEdit_notice->setText("Esse coming out..");
        ui->lineEdit_money->setText(str);
    }
    else
    {
        ui->lineEdit_notice->setText("Not Enough Money");
    }
}

void MainWindow::on_pushButton_select_marlboro_clicked()
{
    int money=ui->lineEdit_money->text().toInt();
    if(money>5000)
    {
        money=money-5000;
        QString str=QString::number(money);
        ui->lineEdit_notice->setText("Marlboro coming out..");
        ui->lineEdit_money->setText(str);
    }
    else
    {
        ui->lineEdit_notice->setText("Not Enough Money");
    }
}

void MainWindow::on_pushButton_selelct_bohem_clicked()
{
    int money=ui->lineEdit_money->text().toInt();
    if(money>4800)
    {
        money=money-4800;
        QString str=QString::number(money);
        ui->lineEdit_notice->setText("Bohem Cigar coming out..");
        ui->lineEdit_money->setText(str);
    }
    else
    {
        ui->lineEdit_notice->setText("Not Enough Money");
    }
}

void MainWindow::on_pushButton_select_mevius_clicked()
{
    int money=ui->lineEdit_money->text().toInt();
    if(money>4500)
    {
        money=money-4500;
        QString str=QString::number(money);
        ui->lineEdit_notice->setText("Mevius Light coming out..");
        ui->lineEdit_money->setText(str);
    }
    else
    {
        ui->lineEdit_notice->setText("Not Enough Money");
    }
}
