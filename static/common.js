function login() {
    var id = document.querySelector('#id');
    var pw = document.querySelector('#pw');

    if(id.value == "" || pw.value == "") {
        alert("등록된 회원 정보가 없습니다.")
    }
    else {
        location.href = 'home.html';
    }
}

function back() {
    history.go(-1);
}

function create_id() {
    var id = document.querySelector('#id');
    var pw = document.querySelector('#pw');
    var r_pw = document.querySelector('#r_pw');
    var name = document.querySelector('#name');

    if (id.value == "")
        alert("id를 입력해주세요.")
    else if (pw.value == "")
        alert("pw를 입력해주세요.")
    else if(pw.value != r_pw.value)
        alert("비밀번호가 동일하지 않습니다.")
    else if (name.value == "")
        alert("이름을 입력해주세요.")
    else 
        location.href = "login.html";
    } 

function add_question() {
    var element = document.getElementsByClassName('answer_hide');
    answer_count = document.getElementsByClassName('answer');
    len=answer_count.length
    if (len==12){
        alert("선택지가 12개보다 많을 수 없습니다!")
    }
    else{
        element[0].className = 'answer'
    }

    }   

function del_question() {
    var element = document.getElementsByClassName('answer');
    len=element.length
    if (len<3){
        alert("선택지가 2개보다 적을 수 없습니다!")
    }
    else{
        element[len-1].className = 'answer_hide'
    }
    }   