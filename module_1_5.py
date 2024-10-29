immutable_var_= (1, 2, 'a', 'b', [2, 4])
print(immutable_var_)
#immutable_var_[1] = 4
#print(immutable_var_)
#Кортёж неизменяем и чаще всего используется как хранилище данных,
# но можно изменить объект внутри кортежа, например, список
#immutable_var_[4:]=6
#immutable_var_[-1:]=6
#immutable_var_[-4:]=6
immutable_var_[-1][-1]=6
immutable_var_[-1][-2]=6
print(immutable_var_)
# не сразу дошло как обратиться к обоим числам из списка,
# не уверен, что это правильно, но вроде получилось.
mutable_list = [1, 7, 'yes']
print(mutable_list)
mutable_list[2] = 5
print(mutable_list)
