
// Your web app's Firebase configuration
var firebaseConfig = {
    apiKey: "AIzaSyDuYp1S1udPe47Idq2zM9FCAg-X3QDUgpw",
    authDomain: "pythondbtest-a8bdf.firebaseapp.com",
    databaseURL: "https://pythondbtest-a8bdf.firebaseio.com",
    projectId: "pythondbtest-a8bdf",
    storageBucket: "pythondbtest-a8bdf.appspot.com",
    messagingSenderId: "418377876568",
    appId: "1:418377876568:web:8c563caf3c401c2b7e762d",
    measurementId: "G-4V1VH879R1"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();
var db = firebase.firestore();
db.collection('notifications').where("is_read", "==", false).onSnapshot(function
    (querySnapshot) {
    var undreaded_box = document.getElementById('undreaded_box');
    undreaded_box.innerHTML = '';
    querySnapshot.forEach(function (snapshot) {
        undreaded_box.innerHTML +=
            `<div id="` + snapshot.id + `" class="alert alert-success" role="alert">
                    <h4 class="alert-heading">New Message</h4>
                    <p>` + snapshot.data().message + `</p>
                    <hr>
                    <a href="#" class="make_as_read_link">Make As Read</a>
                 </div>`;
        $('.make_as_read_link').click(function (e) {
            e.preventDefault();
            makeAsRead(snapshot.id);
        });
    });
});
db.collection('notifications').where("is_read", "==", true).onSnapshot(function
    (querySnapshot) {
    var readed_box = document.getElementById('readed_box');
    readed_box.innerHTML = '';
    querySnapshot.forEach(function (snapshot) {
        readed_box.innerHTML +=
            `<div id="` + snapshot.id + `" class="alert alert-primary" role="alert">
                    <h4 class="alert-heading">Old Message</h4>
                    <p>` + snapshot.data().message + `</p>
                 </div>`;
    });
});

function makeAsRead(snapshot_id) {
    $.ajax("/ajax/make-as-read/?snapshot_id=" + snapshot_id, {
        success: function (data) {
            console.log(data);
        }
    });
}

function sendMessage() {
    /*
    var message_element = document.getElementById('id_message');
    $.ajax('/ajax/send-message?message=' + message_element.value, {
        success: function (data) {
            console.log(data);
            message_element.value = '';
        }
    });*/

    
    let docRef = db.collection('users').doc('alovelace');

    let setAda = docRef.set({
    first: 'Ada',
    last: 'Lovelace',
    born: 1815
    });
    
}