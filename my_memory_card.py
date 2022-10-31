from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QGroupBox,
    QRadioButton, QHBoxLayout, QVBoxLayout, QButtonGroup)
from random import shuffle, randint

class Question: # Soru sınıfının tanımlanması
    def __init__(self, question, right_answer, wrong_answer1, wrong_answer2, wrong_answer3): # Sınıf özelliklerinin dışarıdan alınması
        self.question = question # Sınıf özelliklerinin oluşturulması
        self.right_answer = right_answer # Sınıf özelliklerinin oluşturulması
        self.wrong_answer1 = wrong_answer1 # Sınıf özelliklerinin oluşturulması
        self.wrong_answer2 = wrong_answer2 # Sınıf özelliklerinin oluşturulması
        self.wrong_answer3 = wrong_answer3 # Sınıf özelliklerinin oluşturulması

soru1 = Question("Brezilya'nın resmi dili", "Portekizce", "Türkçe", "Arapça", "İspanyolca") # Birinci sorunun hazırlanması
soru2 = Question("Türkiye'nin başkenti neresidir?", "Ankara", "İstanbul", "İzmir", "Manisa") # İkinci sorunun hazırlanması
soru3 = Question("Rubikon'u geçtik adlı sözü hangi general söylemiştir?", "Sezar", "Atilla", "Napolyon", "III. George") # Üçüncü sorunun hazırlanması
soru4 = Question("Hangisi İskandinav ülkesidir?", "Danimarka", "İngiltere", "Amerika", "Türkiye") # Dördüncü sorunun hazırlanması
soru5 = Question("İstanbul ne zaman fethedilmiştir?", "1453", "1666", "1742", "1899") # Beşinci sorunun hazırlanması
soru6 = Question("Arabaların kaç tekeri vardır?", "4", "8", "2", "10") # Altıncı sorunun hazırlanması
soru7 = Question("Türklerin ilk destanı nedir?", "Yaradılış destanı", "Ergenekon Destanı", "Mansa Destanı", "Şu destanı") # Yedinci sorunun hazırlanması
soru8 = Question("Fenerbahçe en son kaç yılında şampiyon olmuştur?", "2014", "2022", "2019", "1997") # Sekizinci sorunun hazırlanması

soru_listesi = [] # Soruların tutulacağı liste
soru_listesi.append(soru1) # Birinci sorunun listeye eklenmesi
soru_listesi.append(soru2) # İkinci sorunun listeye eklenmesi
soru_listesi.append(soru3) # Üçüncü sorunun listeye eklenmesi
soru_listesi.append(soru4) # Dördüncü sorunun listeye eklenmesi
soru_listesi.append(soru5) # Beşinci sorunun listeye eklenmesi
soru_listesi.append(soru6) # Altıncı sorunun listeye eklenmesi
soru_listesi.append(soru7) # Yedinci sorunun listeye eklenmesi
soru_listesi.append(soru8) # Sekizinci sorunun listeye eklenmesi

application = QApplication([]) # Uygulama nesnesinin oluşturulması

question_label = QLabel("Hangi milliyet yok?") # Soru etiketinin oluşturulması
answer_button = QPushButton("Cevapla") # Cevaplama butonunun oluşturulması
options_groupbox = QGroupBox("Cevap seçenekleri") # Seçeneklerin olacağı grubun oluşturulması

option1_radiobutton = QRadioButton("Enetsler") # Birinci seçeneğin oluşturulması
option2_radiobutton = QRadioButton("Şirinler") # İkinci seçeneğin oluşturulması
option3_radiobutton = QRadioButton("Çulım Tatarları") # Üçüncü seçeneğin oluşturulması
option4_radiobutton = QRadioButton("Aleutlar") # Dördüncü seçeneğin oluşturulması

RadioGroup = QButtonGroup() # Seçenekler için grup oluşturulması
RadioGroup.addButton(option1_radiobutton) # Birinci seçeneğin gruba eklenmesi
RadioGroup.addButton(option2_radiobutton) # İkinci seçeneğin gruba eklenmesi
RadioGroup.addButton(option3_radiobutton) # Üçüncü seçeneğin gruba eklenmesi
RadioGroup.addButton(option4_radiobutton) # Dördüncü seçeneğin gruba eklenmesi

options_groupbox_hlayout = QHBoxLayout() # Yatay düzenin oluşturulması
options_groupbox_vlayout1 = QVBoxLayout() # Dikey düzenin oluşturulmas
options_groupbox_vlayout2 = QVBoxLayout() # Dikey düzenin oluşturulması

options_groupbox_vlayout1.addWidget(option1_radiobutton) # Birinci seçeneğin birinci dikey düzene eklenmesi
options_groupbox_vlayout1.addWidget(option2_radiobutton) # İkinci seçeneğin birinci dikey düzene eklenmesi
options_groupbox_vlayout2.addWidget(option3_radiobutton) # Üçüncü seçeneğin ikinci dikey düzene eklenmesi
options_groupbox_vlayout2.addWidget(option4_radiobutton) # Dördüncü seçeneğin ikinci dikey düzene eklenmesi
options_groupbox_hlayout.addLayout(options_groupbox_vlayout1) # Birinci dikey düzenin yatay düzene eklenmesi
options_groupbox_hlayout.addLayout(options_groupbox_vlayout2) # İkinci dikey düzenin yatay düzene eklenmesi

options_groupbox.setLayout(options_groupbox_hlayout) # Yatay düzenin gruba tanımlanması

results_groupbox = QGroupBox("Test sonucu") # Sonuçların olacağı grubun oluşturulması

result_label = QLabel("Doğru/Yanlış") # Sonuç etiketinin oluşturulması
status_label = QLabel("Doğru cevap") # Durum etiketinin oluşturulması

results_groupbox_layout = QVBoxLayout() # Dikey düzenin oluşturulması
results_groupbox_layout.addWidget(result_label) # Sonuç etiketinin dikey düzene eklenmesi
results_groupbox_layout.addWidget(status_label, alignment=Qt.AlignCenter) # Durum etiketinin dikey düzene eklenemesi

results_groupbox.setLayout(results_groupbox_layout) # Dikey düzenin gruba tanımlanması

main_vlayout = QVBoxLayout() # Ana düzenin oluşturulması
main_vlayout.setSpacing(35) # Düzen ögeleri arasına boşluk eklenmesi
main_vlayout.addWidget(question_label, alignment= Qt.AlignCenter) # Soru etiketinin ana düzene eklenmesi
main_vlayout.addWidget(options_groupbox) # Seçenekler grubunun ana düzene eklenmesi
main_vlayout.addWidget(results_groupbox) # Sonuçlar grubunun ana düzene eklenmesi
button_layout = QHBoxLayout() # Buton düzeninin oluşturulması
button_layout.addStretch(1) # Buton düzenine bir birim boşluk bırakılması
button_layout.addWidget(answer_button, stretch=2) # Butonun buton düzenine eklenmesi ve 2 birim yer kaplamasının sağlanması
button_layout.addStretch(1) # Buton düzenine bir birim boşluk bırakılması
main_vlayout.addLayout(button_layout) # Buton düzeninin ana düzene eklenmesi

def show_result(): # Sonuçların gösterilmesini sağlayan fonksiyon
    options_groupbox.hide() # Seçeneklerin gizlenmesi
    results_groupbox.show() # Sonuçların gösterilmesi
    answer_button.setText("Sonraki Soru") # Buton yazısının değiştirilmesi

def show_question(): # Seçenekleri gösterilmesini sağlayan fonksiyon
    results_groupbox.hide() # Sonuçların gizlenmesi
    options_groupbox.show() # Seçeneklerin gösterilmesi
    answer_button.setText("Cevapla") # Buton yazısının değiştirilmesi
    RadioGroup.setExclusive(False) # Radio Butonların exclusive özelliğinin kapatılması
    option1_radiobutton.setChecked(False) # Butonun işaretinin kaldırılması
    option2_radiobutton.setChecked(False) # Butonun işaretinin kaldırılması
    option3_radiobutton.setChecked(False) # Butonun işaretinin kaldırılması
    option4_radiobutton.setChecked(False) # Butonun işaretinin kaldırılması
    RadioGroup.setExclusive(True) # Radio Butonların exclusive özelliğinin tekrar açılması
   

options = [option1_radiobutton, option2_radiobutton, option3_radiobutton, option4_radiobutton] # Butonların tutulduğu listenin oluşturulması

def ask(soru): # Sorunun tanımlanmasını sağlayan fonksiyon
    question_label.setText(soru.question) # Soru etiketinin güncellenmesi
    shuffle(options) # Soru seçeneklerinin karıştırılması
    options[0].setText(soru.right_answer) # Doğru cevabın yerleştirilmesi
    options[1].setText(soru.wrong_answer1) # Yanlış cevabın yerleştirilmesi
    options[2].setText(soru.wrong_answer2) # Yanlış cevabın yerleştirilmesi
    options[3].setText(soru.wrong_answer3) # Yanlış cevabın yerleştirilmesi
    status_label.setText(soru.right_answer) # Doğru cevabın sonuçlar kısmına yerleştirilmesi
    show_question() # Sorunun gösterilmesi

def check_answer(): # Cevabın kontrol edilmesini sağlayan fonksiyon
    if options[0].isChecked(): # Eğer doğru cevap seçiliyse
        show_correct("Doğru!") # Bilme durumunun belirlenmesi
        widget.skor += 1 # Soru doğru bilindiğinde skorun 1 artırılması
    elif options[1].isChecked() or options[2].isChecked() or options[3].isChecked(): # Eğer yanlış cevaplar seçiliyse
        show_correct("Yanlış!") # Bilme durumunun belirlenmesi
    else: # Eğer hiçbiri seçili değilse
        show_correct("Boş bırakıldı!") # Bilme durumunun belirlenmesi
    print("[----- İstatistikler -----]")
    print("Kullanıcıya sorulan soru sayısı: {}".format(widget.toplam))
    print("Kullanıcının doğru cevap verdiği soru sayısı: {}".format(widget.skor))
    print("Kullanıcının başarı derecesi: {}".format((widget.skor/widget.toplam)*100))

def show_correct(result): # Cevabın doğru olup olmadığını gösteren fonksiyon
    result_label.setText(result) # Bilme durumunun belirlenmesi
    show_result() # Sonuçların gösterilmesi

def next_question(): # Sonraki sorunun gösterilmesini sağlayan fonksiyon
    if len(soru_listesi) == 0: # Eğer soru listesinde sorulacak soru kalmazsa
        print("Sorular bitti.")
    else: # Eğer soru listesinde hala sorulacak soru varsa
        widget.toplam += 1 # Sorulan soru sayısını 1 arttır
        rastgele_sayi = randint(0, len(soru_listesi) - 1) # Sorunun rastgele belirlenmesi için rastgele sayı oluşturulması
        ask(soru_listesi[rastgele_sayi]) # Soru sorma fonksiyonuna rastgele seçilen sorunun gönderilmesi
        del soru_listesi[rastgele_sayi] # Rastgele seçilen sorunun liste içerisinden silinmesi

def click_ok(): # Butona tıklandığında çalıştırılacak fonksiyon 
    if answer_button.text() == "Cevapla": # Eğer buton üzerindeki yazı 'Cevapla' ise
        show_result() # Doğru cevabın gösterilmesi
        check_answer() # Cevabın kontrol edilmesi
    else: # Eğer buton üzerindeki yazı 'Cevapla' değilse
        next_question() # Sonraki soruya geçiş


widget = QWidget() # Pencere nesnesinin oluşturulması
widget.setWindowTitle("Memory Card") # Pencere başlığının düzenlenmesi
widget.setFixedSize(300,200) # Pencere boyutunun düzenlenmesi
widget.setLayout(main_vlayout) # Ana düzenin pencereye tanımlanması
# widget.simdiki_soru = -1 # Uygulama penceresinin özelliği olarak soru sayacının tanımlanması
widget.skor = 0 # Doğru cevap sayısını saklayacak olan değişkenin tanımlanması
widget.toplam = 0 # Toplam sorulan soru sayısını saklayacak olan değişkenin tanımlanması
answer_button.clicked.connect(click_ok) # Cevapla butonuna basıldığında çalıştırılacak fonksiyonun tanımlanması
next_question() # Soru sorma işleminin başlatılması
widget.show() # Pencerenin gösterilmesi
application.exec() # Uygulamanın çalıştırılması