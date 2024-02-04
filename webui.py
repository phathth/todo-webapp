import streamlit as stl
from modules import functions

todos = functions.get_todos()


def main():
    stl.title("My Todo App")    # .title - tra ve 1 "Title" instance
    stl.subheader("This is my Todo App")    # tra ve 1 "Subheader" instance
    stl.write("This Todo app helps to improve productivity")    # tra ve 1 "Text" instance

    for todo in todos:
        check_box = stl.checkbox(todo, key=todo)
        # mac dinh Checkbox se dung noi dung "Text" de lam "key" -> neu co noi dung "Text" trung nhau -> se bao loi & khong tao tiep Checkbox -> dung index de lam "key"
        # khi Checkbox duoc chon -> tra ve True
        if check_box:   # xoa Todo duoc chon bang Checkbox
        # khong dung stl.session_state[todo] duoc vi trong lan load web dau tien, do web chua duoc load het nen "session_state" chua co gia tri nao -> bao loi khi truy xuat "session_state"
        # khi 1 Checkbox duoc chon -> se chay tiep phan code con lai cua script .py sau vong lap "for" (vong lap "for" da duoc chay xong de hien thi het cac Check box truoc do) -> chay lai code tu dau script den vong lap "for" -> kiem tra duoc Checkbox da duoc chon tra ve True
            todos.remove(todo)
            functions.write_todos(todos)
            del stl.session_state[todo]
            # do "session_state" chi duoc cap nhat khi co 1 action duoc thuc hien (ex: Enter trong Input box, chon 1 Check box) hoac browser duoc refresh
            # -> du Todo duoc chon bang Checkbox da duoc xoa va khong con hien thi tren browser nhung van con nam trong "session_state" do chua co action nao tiep theo sau khi vong lap "for" duoc chay xong de hien thi danh sach Check box moi bang lenh "rerun()"
            # -> dung "del" de manually xoa Todo trong "session_state"
            stl.rerun()
            # rerun() - chay tiep code sau do den het va chay lai code tu dau -> vong lap "for" duoc chay de hien thi danh sach Check box moi -> thay duoc Todo duoc chon xoa bang Check box truoc do khong con hien thi tren browser
            # do code khong tu dong chay tiep trong truong hop nay cho Checkbox -> phai buoc code chay tiep bang "rerun()"

    stl.text_input(label="New Todo:", placeholder="Input new Todo ...", key="new_todo", on_change=add_todo)
    # tao Input box - "label" la tieu de; "placeholder" la goi y (hint)
    # on_change=<callback_func> - function se duoc chay khi co thay doi tren Input box (ex: nhan Enter, click chuot ra khoi input box -> toan bo script .py cung se duoc chay cho den het phan con lai va sau do script .py tu dong duoc chay lai tiep)

    # print("hello")  # de kiem tra script .py co bi goi chay het -> xuat "hello" ra man hinh Python khi script duoc chay het
    # stl.session_state   # hien thi cac input data dang duoc luu tru trong session_state len man hinh Web app tren browser ({"new_todo":"Play tennis"})
    # se hien thi truc tuyen data duoc thay doi khi user input trong Web app tren browser
    # giong nhu print(event, values) -> duoc dung de thay duoc gia tri tra ve tu cac elements tren Web app -> dung cac gia tri nay de code


def add_todo():
    new_todo = stl.session_state["new_todo"]
    # session_state - la 1 object chua cac input data cua user o dang <key>:<value> trong do <key> la cua cac elements (ex: input box ...)
    # data duoc luu tru giong nhu 1 dictionary ({"new_todo":"Play tennis"})
    # session_state se monitor & update truc tuyen cac input data khi user input tren web app (giong nhu window.read())
    todos.append(new_todo + "\n")
    functions.write_todos(todos)


main()

