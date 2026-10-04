#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQuickStyle>
int main(int argc,char**argv){QGuiApplication a(argc,argv);QQuickStyle::setStyle("Material");QQmlApplicationEngine e;e.loadFromModule("MD3Reference","Main");return e.rootObjects().isEmpty()?-1:a.exec();}
