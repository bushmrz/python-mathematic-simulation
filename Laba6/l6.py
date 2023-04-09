import numpy as np
from tkinter import *

# класс процессор симулироет отдельный процессор на него поступают заявки он может генерировать такие события как окончание работы и начало работы
class Processor:
    def __init__(self,ver,name):
        self.coof=ver
        self.time_work=0
        self.name=name
        self.enabled=0
        self.orders=0
        self.time_start=0
        self.zakaz=0
        self.mass_orders=0
        self.orders_koll=[]
    def connect_timeline(self,timeline):
        self.timeline=timeline
        # функция для создания события конец обработки задачи
    def start_create_obr(self,time):
        if self.enabled==0:
            self.timeline.add_event({"name":self.name+" конец создания", "time":self.ver(),"functions":[self.end_create_obr]})
            self.enabled=1
            self.time_start = self.timeline.time
            self.orders_koll[0]["time_queue"]=self.orders_koll[0]["time_queue"]+(round(self.timeline.time-self.orders_koll[0]["tec_time"],2))
            # функция для завершения работы и создания события начало работы если в очереди заявок есть заявки
    def end_create_obr(self,time):
        self.time_work =self.time_work+ (time-self.time_start)
        self.orders_koll[0]["time_work"] = self.orders_koll[0]["time_work"] + (time-self.time_start)
        self.enabled=0
        self.pop_orders(0)
        self.zakaz+=1
        if self.orders !=0:
            self.timeline.add_event({"name": self.name + " начало создания", "time": round(time,2), "functions": [self.start_create_obr]})
            # функция получения заявки от системы
    def get_orders(self,time):
        self.orders+=1
        self.timeline.orders_all+=1
        tec_orders=self.timeline.tec_order.copy()
        tec_orders["path"]=tec_orders["path"]+"_"+self.name
        self.orders_koll.append(tec_orders)
        # функция отправки заявки назад в систему
    def pop_orders(self,time):
        self.orders-=1
        self.orders_koll[0]["tec_time"]=self.timeline.time
        self.timeline.tec_order=self.orders_koll.pop(0)
    def get_statistics(self):
        return self.name+"\n     время работы: "+str(self.time_work)+"\n     количество обработанных задач: "+str(self.zakaz)+"\n     количество заявок в очереди: "+str(self.orders)+"\n     коэффициент загрузки: "+str(round(self.time_work/self.timeline.time,2))+"\n     простой: "+str(round((self.timeline.time-self.time_work)/self.timeline.time,2)*100)+"%" + "\n ======================"
    def ver(self):
       return np.random.normal(self.coof[0],self.coof[1])+self.timeline.time


# класс система симулирует систему в целом есть место для хранения всех процессоров он отвечает за обработку событий также сам может генерировать события такие как новая заявка и отправление заявки на процессор и начало работы процессора
class System:
    def __init__(self,mass_proc):
        self.processors=mass_proc
        for i in self.processors:
            i.connect_timeline(self)
        self.enabled=0
        self.orders_all=0
        self.time=0
        self.zakaz=0
        self.history=[]
        self.order_history=[]
        self.tec_order={"path":"","time_queue":0,"time_work":0,"tec_time":round(self.time,2)}
        self.events = [{"name": "заявка", "time": 0, "functions": [self.get_order,self.get_processors]}]
        self.time_work=0
        self.time_save_enable=0
        self.order_stats=0
        self.path=[]
        self.rasp=[]
        # функция для добавления любого события
    def add_event(self,el):
        self.events.append(el)
        self.events.sort(key=lambda x: x["time"])
        # функция для создания события новая заявка
    def get_order(self,time):
        new_time= self.order_stats(self.time)
        self.add_event({"name": "заявка", "time": new_time, "functions":[self.get_order,self.get_processors]})
        # функция для отправки на процессор заявки и включения процессора если он не занят
    def get_processors(self,time):
        tec_proc = self.get_rand_processor()
        self.tec_order = {"path": "", "time_queue": 0, "time_work": 0, "tec_time": round(self.time,2)}
        self.add_event({"name": tec_proc.name+" отправленная заявка", "time": round(self.time,2),"functions": [tec_proc.get_orders]})
        if tec_proc.enabled==0:
            self.add_event({"name": tec_proc.name + " начало создания", "time": round(self.time,2), "functions": [tec_proc.start_create_obr]})
            # функция для отправки на процессор заявки и включения процессора если он не занят
    def get_processors_con(self,proc):
        self.add_event({"name": proc.name + " отправленная заявка", "time": round(self.time,2), "functions": [proc.get_orders]})
        if proc.enabled == 0:
            self.add_event({"name": proc.name + " начало создания", "time": round(self.time,2),"functions": [proc.start_create_obr]})
    def get_rand_processor(self):
        rd = np.random.rand()
        k = 0
        for i in self.rasp:
            if rd >= i[0] and rd < i[1]:
                return self.processors[k]
            k+=1
    def is_enabled(self):
        c=0
        for i in self.processors:
            if i.enabled ==1:
                c=1
        if c == 0 and self.enabled!=0:
            self.time_save_enable = self.time
        elif c==1 and self.enabled!=1:
            self.time_work = self.time_work + (self.time - self.time_save_enable)
        self.enabled=c
        # функция для обработки событий берет первое событие из очереди и обрабатывает его
    def get_tik_simulator(self):
        tec_events = self.events.pop(0)
        self.time = tec_events["time"]
        if tec_events["name"].find("конец создания")!=-1:
            for i in tec_events["functions"]:
                i(round(self.time,2))
            root=[]
            for i in self.path:
                if tec_events["name"].find(i[0])!=-1:
                    root.append(i)
            rand_two=np.random.rand()
            for i in root:
                if rand_two>=i[2] and rand_two<i[3]:
                    if i[1]=="T":
                        self.zakaz += 1
                        self.order_history.append(self.tec_order)
                    else:
                        self.get_processors_con(self.search_process(i[1]))
                    break
        else:
            for i in tec_events["functions"]:
                i(round(self.time,2))
        self.history.append({"name":tec_events["name"],"time":tec_events["time"]})
        self.is_enabled()
    def get_history(self):
        str_rez=""
        for i in self.history:
            str_rez=str_rez+str(i)+"\n"
        return str_rez
    def get_statistic(self):
        str_rez = ""
        for i in self.processors:
            str_rez = str_rez + i. get_statistics() + "\n"
        str_rez = str_rez + "время: "+str(round(self.time,2))+"\nколичество выполненых задач: "+str(self.zakaz)+"\n" + "====================== \n"
        mass_path=set()
        for i in self.order_history:
             mass_path.add(i["path"])
        for i in mass_path:
            mass_con_path=[]
            for j in self.order_history:
                if i==j["path"]:
                    mass_con_path.append(j)
            time_och=0
            time_work=0
            for j in mass_con_path:
                time_och=time_och+j["time_queue"]
                time_work=time_work+j["time_work"]
            kol = len(mass_con_path)
            str_rez = str_rez + "статистика заявок на данном пути: "+ i+"\n     Среднее время очереди: "+ str(time_och/kol)+"\n     Среднее время задачи: "+ str(time_work/kol)+ "\n     Количество заявок: "+str(kol)+"\n     Процентное соотношение относительно всех заявок: "+str(round(kol/len(self.order_history)*100,0))+"%\n" + "=======================\n"
        time_och = 0
        time_work = 0
        for i in self.order_history:
            time_och = time_och + i["time_queue"]
            time_work = time_work + i["time_work"]
        kol = len(self.order_history)
        # str_rez = str_rez + "Статистика по всем заявкам:" + "\n     Среднее время очереди: " + str(time_och / kol) + "\n    Среднее время задачи: " + str(time_work / kol) + "\n<--------------------------------->\n"
        # str_rez = str_rez + "абсолютная пропускная способность: " + str(self.zakaz/self.time)+"\n<--------------------------------->\n"
        # str_rez = str_rez + "относительная пропускная способность: " + str((self.zakaz / self.time)/(self.orders_all/self.time)) + "\n<--------------------------------->\n"
        # str_rez = str_rez + "коэффициент загрузки всей программы: " + str(1-self.time_work/self.time) + "\n<--------------------------------->\n"
        return str_rez
    def get_orders_history(self):
        str_rez = ""
        for i in self.order_history:
            str_rez = str_rez + str(i) + "\n"
        return str_rez

    def get_order_stat(self,val):
        self.order_stats = val
    def set_path(self,val):
        self.path=val
    def set_rasp(self,val):
        self.rasp=val
    def search_process(self,name):
        for i in self.processors:
            if name.find(i.name)!=-1:
                return i
mat=''
def cheak_btn():
    if textbox_opt.get()!='':

        button_ruch.destroy()
        global col_op
        col_op=int(textbox_opt.get())
        textbox_opt.delete(0,'end')
        button_ruch_1.grid(row=0,column=1)

def read_mat():
    if textbox_opt.get() != '':
        global mat
        mat=textbox_opt.get()
        mat=mat.split(',')
        textbox_opt.delete(0, 'end')
        if len(mat)!=3:
            read_mat()
        else:
            button_ruch_1.destroy()
            button_ruch_2.grid(row=0, column=1)

def read_disp():
    if textbox_opt.get() != '':
        global disp
        disp=textbox_opt.get()
        disp=disp.split(',')
        textbox_opt.delete(0, 'end')
        if len(disp)!=3:
            read_disp()
        else:
            button_ruch_2.destroy()
            button_ruch_3.grid(row=0, column=1)

def read_mat_int():
    button_ruch.destroy()
    if textbox_opt.get() != '':
        global mat_int,disp_int,integ_int
        vremen=textbox_opt.get()
        vremen=vremen.split(',')
        textbox_opt.delete(0, 'end')
        if len(vremen)!=3:
            read_mat_int()
        else:
            button_ruch_3.destroy()
            mat_int=float(vremen[0])
            disp_int = float(vremen[1])
            integ_int = float(vremen[2])
            button_ruch_4.grid(row=0, column=1)

# Вероятности выбрать процессоры
def read_proc():
    button_ruch.destroy()
    if textbox_opt.get() != '':
        global ver_proc
        ver_proc=textbox_opt.get()
        ver_proc=ver_proc.split(',')
        textbox_opt.delete(0, 'end')
        if len(ver_proc)!=3:
            read_proc()
        else:

            button_ruch_4.destroy()
            button_ruch_5.grid(row=0, column=1)

# Вероятности перехода из 1 в 2 и 1 в 3
def read_ver():
    button_ruch.destroy()
    if textbox_opt.get() != '':
        global ver_1_2
        ver_1_2=textbox_opt.get()
        ver_1_2=ver_1_2.split(',')
        textbox_opt.delete(0, 'end')
        if len(ver_1_2)!=2:
            read_ver()
        else:
            button_ruch_5.destroy()
            button_ruch_6.grid(row=2, column=0,columnspan=2,stick='we')


def compl():
    global col_op
    global mat
    global disp
    global mat_int, disp_int, integ_int
    global ver_proc
    global ver_1_2
    kolwo_powtor = col_op
    mass_proc = []
    for i in range(1, 4):
        proc1 = int(mat[i-1])
        proc2 = int(disp[i-1])
        mass_proc.append([proc1, proc2])
    task1 = mat_int
    task2 = disp_int
    integ = integ_int
    mass_ver = []
    tec_ver = 0
    for i in range(1, 4):
        tk = float(ver_proc[i-1])
        mass_ver.append([tec_ver, tec_ver + tk])
        tec_ver = tec_ver + tk
    mass_path = []
    mass_path.append(["процессор2", "T", 0, 1])
    mass_path.append(["процессор3", "T", 0, 1])
    ver = float(ver_1_2[0])
    tec_ver = 0
    mass_path.append(["процессор1", "процессор2", tec_ver, tec_ver + ver])
    tec_ver = tec_ver + ver
    ver = float(ver_1_2[1])
    mass_path.append(["процессор1", "процессор3", tec_ver, tec_ver + ver])
    tec_ver = tec_ver + ver
    time = 0
    absolutle = 0
    otnos = 0
    koof_zag = 0
    timeline = 0
    for j in range(1, kolwo_powtor + 1):
        kol = 1
        processors = []
        for i in mass_proc:
            processor = Processor(i, "процессор" + str(kol))
            processors.append(processor)
            kol += 1
        timeline = System(processors)

        timeline.get_order_stat(lambda x: np.random.normal(loc=task1, scale=task2) + x)
        timeline.set_rasp(mass_ver)
        timeline.set_path(mass_path)

        while timeline.zakaz != integ:
            timeline.get_tik_simulator()
        time = time + timeline.time
        absolutle = absolutle + (timeline.zakaz / timeline.time)
        otnos = otnos + ((timeline.zakaz / timeline.time) / (timeline.orders_all / timeline.time))
        koof_zag = koof_zag + (1 - timeline.time_work / timeline.time)
    label1 = Text(add,width=80, height=12)
    label1.insert(1.0,timeline.get_history())
    label2 = Text(add,width=115, height=12)
    label2.insert(1.0, timeline.get_orders_history())
    # label3 = Text(add,width=80, height=10)
    # label3.insert(1.0,timeline.get_history())
    label4 = Text(add,width=80, height=15)
    label4.insert(1.0,timeline.get_statistic())
    label5 = Label(add, text="время работы программы в среднем: " + str(time / kolwo_powtor))
    label6 = Label(add, text=str("абсолютная пропускная способность в среднем: " + str(absolutle / kolwo_powtor)))
    label7 = Label(add, text=str("абсолютная относительная способность в среднем: " + str(otnos / kolwo_powtor)))
    label8 = Label(add, text=str("коэффициент загрузки всей программы в среднем: " + str(koof_zag / kolwo_powtor)))
    label1.grid(row=3, column=0)
    label2.grid(row=4, column=0)
    # label3.grid(row=5, column=0)
    label4.grid(row=6, column=0)
    label5.grid(row=7, column=0)
    label6.grid(row=8, column=0)
    label7.grid(row=9, column=0)
    label8.grid(row=10, column=0)
    label_mat=Label(add, text=("Матем ожид= "+str(mat)))
    label_col = Label(add, text=("Количество= " + str(col_op)))
    label_disp = Label(add, text=("Дисперсия= " + str(disp)))
    label_ = Label(add, text=("Матем инте, дисп, колл_деталей " + str(mat_int)+" "+str(disp_int)+" " +str(integ_int)))
    label_ver=Label(add, text=("Вероятности - " + str(ver_proc)))
    label_ver_proc = Label(add, text=("Вероятности перехода- " + str(ver_1_2)))
    label_mat.grid(row=11, column=0)
    label_col.grid(row=12, column=0)
    label_disp.grid(row=13, column=0)
    label_.grid(row=14, column=0)
    label_ver.grid(row=15, column=0)
    label_ver_proc.grid(row=16, column=0)
    # print(timeline.get_history())
    # print(timeline.get_orders_history())
    # print(timeline.get_history())
    # print(timeline.get_statistic())
    # print("время работы программы в среднем: " + str(time / kolwo_powtor))
    # print("абсолютная пропускная способность в среднем: " + str(absolutle / kolwo_powtor))
    # print("абсолютная относительная способность в среднем: " + str(otnos / kolwo_powtor))
    # print("коэффициент загрузки всей программы в среднем: " + str(koof_zag / kolwo_powtor))

def defal():
    global col_op
    global mat
    global disp
    global mat_int, disp_int, integ_int
    global ver_proc
    global ver_1_2
    col_op=200
    mat='4,3,5'
    mat=mat.split(',')
    disp='1,1,2'
    disp=disp.split(',')
    mat_int=3
    disp_int=1
    integ_int=200
    ver_proc='0.4,0.3,0.3'
    ver_proc=ver_proc.split(',')
    ver_1_2='0.3,0.7'
    ver_1_2=ver_1_2.split(',')
    button_ruch_6.grid(row=2, column=0, columnspan=2, stick='we')

def destroy_button():
    add_inputs.destroy()

def destroy_all():
    button_ruch.destroy()
    button_ruch_1.destroy()
    button_ruch_2.destroy()
    button_ruch_3.destroy()
    button_ruch_4.destroy()
    button_ruch_5.destroy()
    create_button()




def create_button():
    global button_ruch,button_ruch_1, button_ruch_2, button_ruch_3, button_ruch_4, button_ruch_5
    destroy_button()

    button_ruch_1 = Button()
    button_ruch_2 = Button()
    button_ruch_3 = Button()
    button_ruch_4 = Button()
    button_ruch_5 = Button()
    button_ruch = Button(add, text="Ввести значения с клавиатуры(Количество опытов)", command=cheak_btn)
    button_ruch.grid(row=0, column=1)
    button_ruch_1 = Button(add, text="Ввести значения с клавиатуры(Введите значения мат ожидания времени работы)",
                           command=read_mat)
    button_ruch_2 = Button(add, text="Ввести значения с клавиатуры(Введите значения Дисперсии)", command=read_disp)
    button_ruch_3 = Button(add,
                           text="Ввести значения с клавиатуры(Введите значение мат ожидания интенсивности поступления задачи,дисперсию и колличество деталей)",
                           command=read_mat_int)
    button_ruch_4 = Button(add, text="Вероятности выбрать процессоры", command=read_proc)
    button_ruch_5 = Button(add, text="Вероятности перехода из 1 в 2 и 1 в 3", command=read_ver)





add=Tk()
add.title("Machine")
add.geometry("1000x1000")

button_standart=Button(add, text="Стандартные значения", command=defal)
button_standart.grid(row=0,column=0)
add_inputs = Button(add, text="Ввести значения с клавиатуры", command=create_button)
add_inputs.grid(row=0, column=1)
# button_ruch = Button()
button_ruch_7 = Button(add, text="Сброс", command=destroy_all)
button_ruch_7.grid(row=0, column=3)

button_ruch_6 = Button(add, text="Посчитать", command=compl)
textbox_opt=Entry(add, width=15)
textbox_opt.grid(row=1,column=1)
add.mainloop()
col_op=0
disp=''
mat_int=0
disp_int=0
integ_int=0
ver_proc=''
ver_1_2=''
