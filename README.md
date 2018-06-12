# flexsible-box
1) Здесь реализован каркас для проекта в котором периодически у сущностей добавляются/удаляются поля или редактируются параметры этих полей. Сами поля имеют простые типы и служат только для структурированного хранения информации. Для поддержки актуальной схемы валидации со стороны BackEnd при минимальных временных затратах - управление набором полей было вынесено в админку. Есть 3 абстрактных класса AbstractOperation (каркас для самой сущности), AbstractOperationType (каркас для группы параметров),  AbstractParameter (каркас для самого параметра, который создаётся и редактируется в админке). 
Например на основе этой концепции создадим InsuredObject. Наследуясь от AbstractOperation создаётся InsuredObject (страховой объект у которого куча изменяющихся параметров, наследуясь от AbstractOperationType создаётся InsuredObjectType (это группа параметров для InsuredObject), наследуясь от AbstractParameter создаётся InsuredObjectParameter. Теперь через админку администратор системы может создавать и изменять сколько угодно InsuredObjectParameter c настройками(Integer, is_required, is_many и т.д.) и привязывать их к InsuredObjectType. Теперь в момент создания самой сущности InsuredObject через API сервера - класс ParametersValidator сам подтянет через InsuredObjectType привязанные InsuredObjectParameter и по ним свалидирует входящие значения.

2) Здесь на основе Django REST framework реализован класс NestedModelSerializer, который создаёт вложенные сущности по связям ForeignKey и ManyToMany (на подобии GraphQL)
