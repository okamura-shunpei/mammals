function connecttext( textid, ischecked ) {
                if( ischecked == true ) {
                    // チェックが入っていたら有効化
                    document.getElementById(textid).disabled = false;
                    }
                else {
                        // チェックが入っていなかったら無効化
                    document.getElementById(textid).disabled = true;
                    }
            }
            function connecttext_invert( textid, ischecked ) {
                if( ischecked == true ) {
                    // チェックが入っていたら有効化
                    document.getElementById(textid).disabled = true;
                    }
                else {
                        // チェックが入っていなかったら無効化
                    document.getElementById(textid).disabled = false;
                    }
            }
            function isCheck() {
                let arr_checkBoxes_list = [document.getElementsByClassName("check_content"), document.getElementsByClassName("check_format"), document.getElementsByClassName("check_treatment"), document.getElementsByClassName("check_gender"), document.getElementsByClassName("check_place"), ];
                let count = 0;
                for (let j = 0; j < arr_checkBoxes_list.length; j++) {
                    arr_checkBoxes = arr_checkBoxes_list[j];
                    for (let i = 0; i < arr_checkBoxes.length; i++) {
                        if (arr_checkBoxes[i].checked) {
                            count++;
                        }
                    }
                }
                if (count > 0) {
                    return true;
                } else {
                    window.alert("1つ以上選択してください。");
                    return false;
                };
            }