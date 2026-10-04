#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQuickStyle>
int main(int argc,char *argv[]){QGuiApplication app(argc,argv);QQuickStyle::setStyle("Material");QQmlApplicationEngine engine;engine.loadFromModule("MD3Catalog","Main");if(engine.rootObjects().isEmpty())return -1;return app.exec();}
