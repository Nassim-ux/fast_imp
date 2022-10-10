//import related modules
import QtQuick
import QtQuick.Controls

//window containing the application
ApplicationWindow {

    visible: true

    //title of the application
    title: qsTr("fastIMP")
    width: 640
    height: 480

    //menu containing two menu items
    menuBar: MenuBar {
        Menu {
            title: qsTr("File")
            MenuItem {
                text: qsTr("&Open")
                onTriggered: console.log("Open action triggered");
            }
            MenuItem {
                text: qsTr("Exit")
                onTriggered: Qt.quit();
            }
        }
    }

    //Content Area
    TextInput {
        id: email__input
        text: "email"
        y: 30
        cursorVisible: false
        anchors.horizontalCenter: parent.horizontalCenter
    }

    TextInput {
        id: password__input
        text: "password"
        y: 60
        cursorVisible: false
        echoMode: TextInput.Password
        anchors.horizontalCenter: parent.horizontalCenter
    }
    //a button in the middle of the content area
    Button {
        text: qsTr("login")
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
    }
}
       