from collections import deque
def palindrome(palabra):
	cola = deque([])
	pila =[]
	p=0
	for i in palabra:
		cola.append(i)
		pila.append(i)
	for i in palabra:
		if cola.popleft()==cola.pop:
			p+=1
	if p==len(palabra):
		return True
	else:
		return False

palabra=input("palabra= ")
print (palindrome(palabra))