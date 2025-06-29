# Название приложения   
Короткое описание приложения  

## Содержание  

[Разделы]()  
[Развернуть проект]()  
[Создание пользователей]()  
[Наполнение базы данных]()  
[Redis]()  
[Запуск приложения]()  
[Возможности]()  
[Модели]()  
[Пагинация]()  
[Представления](#Представления)  


----
## Разделы  


----
## Развернуть проект



----
## Представления 

### reference application  
**CBV:**  
**BoxSummaryCreateView**  
Представление управляет отображением страницы создания записи о материале короба  
Шаблоны:    
    - box/box_reference_create.html  
Модели:  
    - BoxSummary  
Формы:  
    - UpdateBoxSummaryForm  
  
  
**BoxSummaryUpdateView**  
Представление управляет отображением страницы обновления записи о материале короба  
Шаблоны:  
    - box/box_reference_update.html  
Модели:  
    - BoxSummary  
Формы:  
    - UpdateBoxSummaryForm  
  
  
**DoorSummaryCreateView**   
Представление управляет отображением страницы создания записи о материале двери  
Шаблоны:    
    - door/door_reference_create.html  
Модели:  
    - DoorSummary  
Формы:  
    - UpdateDoorSummaryForm  
  
  
**DoorSummaryUpdateView**  
Представление управляет отображением страницы обновления записи о материале двери  
Шаблоны:  
    - door/door_reference_update.html  
Модели:  
    - DoorSummary  
Формы:  
    - UpdateDoorSummaryForm  
  
  
**FBV:**  
**boxsummary_show_view**  
Представление управляет отображением страницы таблицы материалов короба  
  
  
**boxsummary_delete_view**   
Представление управляет удалением записи из таблицы материалов короба  
  
  
**doorsummary_show_view**  
Представление управляет отображением страницы таблицы материалов дверей  


**doorsummary_delete_view**   
Представление управляет удалением записи из таблицы материалов дверей  
  
  
  
### wardrobe  
**CBV:**  
**WardrobeView**  
Представление управляет отображением страницы калькулятора шкафа  
Шаблоны:   
    - wardrobe.html         - страница калькулятора  
    - wardrobe_result.html  - страница результатов расчета  
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
  
  
**WardrobeSaveOrderView** 
Представление управляет страницей сохранения заказа  
Шаблоны:  
    - wardrobe_save_order.html  -  
Модели:  
    - Orders   
Формы:  
    - SaveOrderForm  
  
  
**WardrobeOrderDetailView**   
Представление управляет страницей деталей заказа (данные заказчика и смета)  
Шаблоны:  
    - wardrobe_order_details.html   
Модели:  
    - Orders    
  
  
**OrderUpdateView**   
Представление управляет страницей обновления данных заказа  
Шабоны:  
    - wardrobe_order_update.html  
Модели:  
    - Orders   
Формы:  
    - OrderUpdateForm  
  
  
**FBV:**  
**orders_list_view**     
Представление управляет страницей таблицы заказов   
  
  
**order_delete_view**    
Представление управляет страницей удаления заказа  
  
  
**save_order_success_view**    
Представление управляет страницей, сообщающей об удачном сохранении заказа   
  
  
**combination_not_found_view**    
Представление управляет страницей, сообщающей об отсутствии компонентов по сочетанию характеристик  
