# Название приложения   
Короткое описание приложения  

## Содержание  

[Разделы](#Разделы)  
[Развернуть проект](#Развернуть-проект)  
[Создание пользователей](#Создание-пользователей)  
[Наполнение базы данных](#Наполнение-базы-данных)  
[Redis]()  
[Запуск приложения]()  
[Возможности]()  
[Приложения](#Приложения)  
[Модели](#Модели)  
[Views](#Views)  



----
## Разделы    
1. Справочные материалы      
2. Калькуляторы  
3. Компоненты мебели  
4. Заказы  



----
## Развернуть проект  



---
## Создание пользователей  
Поскольку стандартная модель пользователей была переопределена, создание пользователя администратора для доступа к админке осуществляется командой:   

    python manage.py ccsu  

Учетные данные администратора для авторизации    

    login: top-academy-roman@yandex.ru  
    pass: qwerty  

Все остальные пользователи могут быть созданы с помощью возможности регистрации пользователя на сайте.  


----  
## Наполнение базы данных  



----
## Приложения  
**users**  
Приложение для управления пользователями  

**furniture**  
Приложение для управления наполнением сайта   

**reference**  
Приложение для управления справочниками  

**wardrobe**  
Приложение для рассчета стоимости шкафа и управления заказами на шкафы  



____
## Модели  

### users app   
Users model:   

    - first_name            - имя пользователя    
    - last_name             - фамилия пользователя    
    - email                 - email пользователя    
    - phone                 - телефон пользователя    
    - telegram              - telegram пользователя    
    - is_active             - активность пользователя    

### furniture app   
Furniture model:    

    - name                  - название объекта мебели    
    - description           - описание объекта мебели    
    - image                 - изображение объекта мебели    

### reference app   
MaterialType model:  

    - name                  - название материала  

MaterialThickness model:  

    - thickness             - толщина материала  

MaterialColor model:  

    - name                  - название цвета материала  

DoorType model:  

    - name                  - название типа дверей  

BoxSummary model:
Материалы короба  

    - material_type         - id названия материала (внешняя ссылка на MaterialType)    
    - material_thickness    - id толщины материала (внешняя сслыка на MaterialThickness)    
    - material_color        - id цвета материала (внешняя ссылка на MaterialColor)   
    - price_per_sqm         - цена за квадратный метр для текущей комбинации тип, толщина, цвет    

DoorSummary model:  
Материалы дверей  

    - material_type         - id названия материала (внешняя ссылка на MaterialType)    
    - material_thickness    - id толщины материала (внешняя сслыка на MaterialThickness)    
    - material_color        - id цвета материала (внешняя ссылка на MaterialColor)    
    - door_type             - id типа двери (внешняя ссылка на DoorType)  
    - price_per_sqm         - цена за квадратный метр для текущей комбинации тип, толщина, цвет, цвет двери  

DoorHandle model:  
Дверные ручки  

    - name                  - название дверной ручки  
    - length                - длинна дверной ручки  
    - material              - материал дверной ручки  
    - color                 - цвет  
    - price_per_one         - цена за единицу  

### wardrobe app
Orders model:
Таблица заказов

    - customer_name             - имя заказчика  
    - customer_surname          - фамилия заказчика  
    - phone                     - телефон заказчика  
    - email                     - email заказчика  
    - height                    - высота шкафа  
    - width                     - ширина шкафа  
    - depth                     - глубина шкафа  
    - material_type             - тип материала короба  
    - box_material_thickness    - толщина материала короба  
    - box_material_color        - цвет материала короба  
    - box_square                - общая площадь короба  
    - box_price_per_sqm         - стоимость комбинации материала короба за м.кв.  
    - box_price                 - общая стоимость короба  
    - door_type                 - тип дверей  
    - door_material_thickness   - толщина материала дверей  
    - door_material_color       - цвет материала дверей  
    - door_square               - общая площадь дверей  
    - door_price_per_sqm        - стоимость комбинации материала дверей за м.кв.  
    - door_price                - общая стоимость дверей  
    - handle_name               - название дверной ручки  
    - handle_material           - материал дверной ручик  
    - handle_color              - цвет дверной ручки  
    - handle_length             - длинна дверной ручки (опционально)  
    - handle_price_per_one      - стоимость дверной ручки за единицу  
    - handle_ammount            - количество используемых ручек  
    - handle_price              - обшая стоимость дверных ручек  
    - total_price               - общая стоимость шкафа  
    - owner                     - сотрудник, создавший заказ  
    - order_date                - дата создания заказа 
    - is_active                 - активность заказа



----
## Views     
Представления  


### furniture app  
**IndexView (CBV)**  
Представление управляет отображением главной страницы    

    Шаблоны:  
        - furniture/index.html  
    Модели:  
        - Furniture 


**wardrobe_man_view (FBV)**  
Представление управляет отображением страницы справки для калькулятора шкафа    


**dresser_man_view (FBV)**  
Представление управляет отображением страницы справки для калькулятора комода  


**kitchen_man_view (FBV)**  
Представление управляет отображением страницы справки для калькулятора кухни  


**dresser_calc_plug_view (FBV)**  
Представление управляет отображением страницы-заглушки калькулятора комода  


**kitchen_calc_plug_view (FBV)**  
Представление управляет отображением страницы-заглушки калькулятора кухни  


**dresser_orders_plug_view (FBV)**  
Представление управляет отображением страницы-заглушки заказов комода  


**kitchen_orders_plug_view (FBV)**  
Представление управляет отображением страницы-заглушки заказов кухни  


**dresser_deactivated_plug_view (FBV)**  
Представление управляет отображением страницы-заглушки отмененных заказов комодов  


**kitchen_deactivated_plug_view (FBV)**  
Представление управляет отображением страницы-заглушки отмененных заказов кухни  


### users app  
**UserProfileView (CBV)**    
Представление управляет страницей обновления профиля пользователя    
Страница отображения профиля пользователя предполагает изменения (update) части данных пользователя на текущей странице    

    Шаблоны:  
        - users/user_profile.html  
    Модели:  
        - User   
    Формы:    
        - UserUpdateForm  


**user_register_view (FBV)**  
Представление управляет регистрацией пользователя  


**user_login_view (FBV)**  
Представление управляет авторизацией пользователя  


**successful_register_view (FBV)**  
Представление управляет отображаением страницы успешной регистрации  


**restore_password_view (FBV)**  
Представление управляет отображением страницы восстановления пароля


**user_logout_view (FBV)**  
Представление управляет выходом из профиля пользователя  


**manage_users_view (FBV)**  
Представление управляет страницей управления пользователями (только для администратора)  


**toggle_user_active_view (FBV)**  
Представление управляет страницей переключения активности пользователя (только для администратора) 
 

### reference app     
**BoxSummaryCreateView (CBV)**     
Представление управляет отображением страницы создания записи о материале короба  

    Шаблоны:    
        - box/box_reference_create.html  
    Модели:  
        - BoxSummary  
    Формы:  
        - UpdateBoxSummaryForm  
  
  
**BoxSummaryUpdateView (CBV)**  
Представление управляет отображением страницы обновления записи о материале короба  

    Шаблоны:
        - box/box_reference_update.html  
    Модели:  
        - BoxSummary  
    Формы:  
        - UpdateBoxSummaryForm  
  
  
**DoorSummaryCreateView (CBV)**   
Представление управляет отображением страницы создания записи о материале двери  

    Шаблоны:    
        - door/door_reference_create.html  
    Модели:  
        - DoorSummary  
    Формы:  
        - UpdateDoorSummaryForm  
  
  
**DoorSummaryUpdateView (CBV)**  
Представление управляет отображением страницы обновления записи о материале двери  

    Шаблоны:  
        - door/door_reference_update.html  
    Модели:  
        - DoorSummary  
    Формы:  
        - UpdateDoorSummaryForm  


**HandlesCreateView (CBV)**  
Представление управляет отображением  страницы создания записи о мебельной ручке 

    Шаблоны:  
        - fitting/fit_reference_create.html  
    Модели:  
        - DoorHandle
    Формы:  
        - UpdateFittingForm 


**HandlesUpdateView (CBV)**  
Представление управляет отображением страницы обновления записи о мебельной ручке

    Шаблоны:  
        - fitting/fit_reference_update.html  
    Модели:  
        - DoorHandle
    Формы:  
        - UpdateFittingForm  
  

**boxsummary_show_view (FBV)**   
Представление управляет отображением страницы таблицы материалов короба  
  
  
**boxsummary_delete_view (FBV)**   
Представление управляет удалением записи из таблицы материалов короба  
  
  
**doorsummary_show_view (FBV)**  
Представление управляет отображением страницы таблицы материалов дверей  


**doorsummary_delete_view (FBV)**   
Представление управляет удалением записи из таблицы материалов дверей


**handles_show_view (FBV)**  
Представление управляет отображением страницы мебельных ручек  


**handles_delete_view (FBV)**  
Представление управляет удалением мебельной ручки 


**properties_show_view (FBV)**  
Представление управляет отображением страницы со свойствами материалов  

 
### wardrobe app  
**WardrobeView (CBV)**   
Представление управляет отображением страницы калькулятора шкафа  

    Шаблоны:   
        - wardrobe.html   
        - wardrobe_result.html  
    Модели:  
        - MaterialType   
        - MaterialThickness  
        - MaterialColor  
        - DoorType   
        - BoxSummary   
        - DoorSummary   
        - DoorHandle   
    Формы:  
        - WardrobeForm  
  
  
**WardrobeSaveOrderView (CBV)**  
Представление управляет страницей сохранения заказа  

    Шаблоны:  
        - wardrobe_save_order.html  
    Модели:  
        - Orders   
    Формы:  
        - SaveOrderForm  
  
  
**WardrobeOrderDetailView (CBV)**   
Представление управляет страницей деталей заказа (данные заказчика и смета)  

    Шаблоны:  
        - wardrobe_order_details.html   
    Модели:  
        - Orders    
  
  
**WardrobeOrderUpdateView (CBV)**   
Представление управляет страницей обновления данных заказа  

    Шабоны:  
        - wardrobe_order_update.html  
    Модели:  
        - Orders   
    Формы:  
        - OrderUpdateForm  


**WardrobeDeactivatedDetailView (CBV)**  
Представление управляет страницей деталей отмененного заказа

    Шабоны:  
        - wardrobe_deactivated_order_details.html  
    Модели:  
        - Orders   

  
**wardrobe_orders_list_view (FBV)**    
Представление управляет страницей таблицы заказов   
  
  
**wardrobe_order_delete_view (FBV)**    
Представление управляет страницей удаления заказа  
  
  
**save_order_success_view (FBV)**    
Представление управляет страницей, сообщающей об удачном сохранении заказа   
  
  
**combination_not_found_view (FBV)**    
Представление управляет страницей, сообщающей об отсутствии компонентов по сочетанию характеристик  


**wardrobe_deactivated_list_view (FBV)**  
Представление управляет страницей таблицы отмененных заказов  


**toggle_order_active_view (FBV)**  
Представление управляет переключением активности заказов
