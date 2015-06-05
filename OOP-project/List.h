#ifndef LIST_H
#define LIST_H

#include<iostream>
#include<string>

using namespace std;

template<class T> 
class List
{
public:

	struct Node
	{
	public:
		//конструктор
		Node(const T& m_data, Node* next = NULL, Node* prev = NULL) : m_data(m_data), m_next(next), m_prev(prev){}
		//деструктор
		~Node(){}
		//функция за достъп по член-променливата m_data
		T getData()
		{
			return this->m_data;
		}
		//функция за достъп по член-променливата m_next
		Node* getNext()
		{
			return this->m_next;
		}
		//функция за достъп по член-променливата m_prev
		Node* getPrev()
		{
			return this->m_prev;
		}

		void setNext(Node* next)
		{
			this->m_next = next;
		}

		void setPrev(Node* prev)
		{
			this->m_prev = prev;
		}

	private:
		T m_data;
		Node* m_next;
		Node* m_prev;

	};

	//конструктор, деструктор, конструктор за копиране и конструктор за присвояване
	List();
    ~List();
	List(const List<T>&  ptr);
	List& operator=(const List<T>& right);

	//функция за копиране на списъка, която ще се извиква при конструктора за копиране
	void copyList(const List<T>&);
	//функция за изтриване на списъка
	void deleteList();

	//добавя елемент в началото на списъка
	void push_front(const T& value);
	//премахва елемент в началото на списъка
	void pop_front();
	//добавя елемент в края на списъка
	void push_back(const T& value);
	//премахва елемент в края на списъка
	void pop_back();

	//връща стойността на елемента в началото на списъка
	T front();
	//връща стойността на елемента в края на списъка
	T back();

	class Iterator
	{
	public:
		Iterator();
		Iterator(Node*);

		T operator*();
		//префиксен оператор за инкрементиране (it = ++v.begin())
		Iterator& operator++()
		{
			this->current = this->current->getNext();
			return (*this);
		}
		// постфиксен оператор за инкрементиране(it = v.begin()++)
		Iterator operator++(int)
		{
			Iterator temp = *this;
			++*this;
			return temp;
		}
		//проверява дали адресите на два Node-a са различни
		bool operator!=(const Iterator& temp);
		//помощни функции за вземане на указателя към даден елемент
		Node* getCurrent()
		{
			return this->current;
		}
		void setCurrent(Node* temp)
		{
			this->current = temp;
		}

	private:
		Node* current; //за сегашен елемент

	friend class List<T>;
	};

	//връща iterator към началото на списъка
	Iterator begin()
	{
		return Iterator(start);
	}
	//връща iterator към края на списъка(един елемент след края на списъка)
	Iterator end()
	{
		return Iterator(end);
	}
	//вмъква елемент със стойност value на позиция iterator
	void insert(Iterator& it, const T& value); 
	//изтрива елемент на позиция iterator
	void erase(Iterator it); 
	//връща броя елементи в списъка
	int getSize(); 
	//изтрива всички елементи на списъка
	void clear(); 
	//проверява дали списъка е празен
	bool empty(); 

private:
	unsigned int size; //брояч за елементите на списъка
	Node* start;
	Node* end;
};


//реализация на class List
template<class T>
List<T>::List() : size(0), start(NULL), end(NULL)
{
}

template<class T>
List<T>::~List()
{
	deleteList();
}

template<class T>
List<T>::List(const List<T>& ptr)
{
	copyList(ptr);
}

template <class T>
List<T>& List<T>::operator=(const List<T>& right)
{
	if (this != &right)
	{
		deleteList();
		copyList(right);
	}
	return *this;
}

template <class T>
void List<T>::copyList(const List<T>& original)
{
	Node *ptr_new;
	Node *current;

	if (start != NULL)
	{
		deleteList();
	}

	if (original.start == NULL)
	{
		start = NULL;
		end = NULL;
		size = 0;
		return;
	}

	//Създаване(копиране) на първия възел
	current = original.start;
	start = new Node(current->m_data);
	end = start;

	current = current->m_next;
	while (current != NULL)
	{
		//Създава се нов възел
		ptr_new = new Node(current->m_data);
		end->m_next = ptr_new; //Връзка на предходния с новия възел
		ptr_new->m_prev = end; //Връзка на новия с предходния възел
		end = ptr_new;

		current = current->m_next;
	}
	size = original.size;
}

template<class T>
void List<T>::deleteList()
{
	Node *p;

	while (start != end)
	{
		p = start;
		start = start->getNext();
		delete p;
		p = NULL;
	}
	delete end;
	end = NULL;
	size = 0;
}

template<class T>
void List<T>::push_front(const T& value)
{
	if (start == NULL)
	{
		start = new Node(value);
		end = start;
	}
	else
	{
		Node* ptr_start = start;
		start = new Node(value, start);
		Node* temp = ptr_start->getPrev();
		temp = start;
	}
	this->size++;
}

template<class T>
void List<T>::pop_front()
{
	if (start == NULL)
	{
		return;
	}
	else if (start->getNext() == NULL)
	{
		start = NULL;
		end = NULL;
		delete start;
	}
	else
	{
		Node* temp = start;
		start = start->getNext();
		delete temp;
	}
	size--;
}

template<class T>
void List<T>::push_back(const T& value)
{
	if (start == NULL)
	{
		start = new Node(value);
		end = start;
	}
	else
	{
		Node* temp = new Node(value, NULL, end);
		end->setNext(temp);
		end = temp;
	}
	size++;
}

template<class T>
void List<T>::pop_back()
{
	if (start == NULL)
	{
		return;
	}
	else if (start->getNext() == NULL)
	{
		delete start;
		start = NULL;
		end = NULL;
	}
	else
	{
		Node* ptr_last = end;
		Node* ptr_prev = end->getPrev();
		end = ptr_prev;
		Node* temp = end->getNext();
		temp = NULL;
		delete ptr_last;
	}
	size--;
}

template<class T>
T List<T>::front()
{
	return start->getData();
}

template<class T>
T List<T>::back()
{
	return end->getData();
}

template<class T>
void List<T>::insert(Iterator& it, const T& value)
{
	Node* insNode = new Node(value, NULL, NULL);
	if (it.getCurrent() == NULL)
	{
		it.getCurrent()->setPrev(insNode);
		insNode->setNext(it.getCurrent());
		this->start = insNode;
		this->size++;

	}
	else if (it.getCurrent()->getNext() == NULL)
	{
		it.getCurrent()->setNext(insNode);
		insNode->setPrev(it.getCurrent());
		this->end = insNode;
		this->size++;
	}
	else
	{
		Node* prev = it.getCurrent()->getPrev();
		it.getCurrent()->setPrev(insNode);
		prev->setNext(insNode);

		insNode->setNext(it.getCurrent());
		insNode->setPrev(prev);
		this->size++;
	}
	it.setCurrent(insNode); //за да стои на една и съща позиция
}

template<class T>
void List<T>::erase(Iterator it)
{
	if (it.getCurrent()->getPrev() == NULL) // проверява се дали итератора е в началото на списъка
	{
		it.setCurrent(it.getCurrent()->getNext());
		it.getCurrent()->setPrev(NULL);
		this->start = it.getCurrent();
	}
	else if (it.getCurrent()->getNext() == NULL) // проверява се дали итератора е в края на списъка
	{
		it.setCurrent(it.getCurrent()->getPrev());
		it.getCurrent()->setNext(NULL);
		this->end = it.getCurrent();
	}
	else                                       // ако итератора е в средата на списъка
	{
		it.getCurrent()->getPrev()->setNext(it.getCurrent()->getNext());
		it.getCurrent()->getNext()->setPrev(it.getCurrent()->getPrev());
		Node* temp = it.getCurrent()->getNext();
		delete it.getCurrent();
		it.setCurrent(temp);
	}
	this->size--;
}

template<class T>
int List<T>::getSize()
{
	return this->size;
}

template<class T>
void List<T>::clear()
{
	delete this;
}

template<class T>
bool List<T>::empty()
{
	return start == NULL;
}


//реализация на class Iterator
template<class T>
List<T>::Iterator::Iterator() : current(NULL)
{
}

template<class T>
List<T>::Iterator::Iterator(Node* data) : current(data)
{
}

template<class T>
T List<T>::Iterator::operator*()
{
	return current->getData();
}

template<class T>
bool List<T>::Iterator::operator!=(const Iterator& temp)
{
	return this->current != temp.current;
}

#endif