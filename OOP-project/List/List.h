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
		//�����������
		Node(const T& m_data, Node* next = NULL, Node* prev = NULL) : m_data(m_data), m_next(next), m_prev(prev){}
		//����������
		~Node(){}
		//������� �� ������ �� ����-������������ m_data
		T getData()
		{
			return this->m_data;
		}
		//������� �� ������ �� ����-������������ m_next
		Node* getNext()
		{
			return this->m_next;
		}
		//������� �� ������ �� ����-������������ m_prev
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

	//�����������, ����������, ����������� �� �������� � ����������� �� �����������
	List();
    ~List();
	List(const List<T>&  ptr);
	List& operator=(const List<T>& right);

	//������� �� �������� �� �������, ����� �� �� ������� ��� ������������ �� ��������
	void copyList(const List<T>&);
	//������� �� ��������� �� �������
	void deleteList();

	//������ ������� � �������� �� �������
	void push_front(const T& value);
	//�������� ������� � �������� �� �������
	void pop_front();
	//������ ������� � ���� �� �������
	void push_back(const T& value);
	//�������� ������� � ���� �� �������
	void pop_back();

	//����� ���������� �� �������� � �������� �� �������
	T front();
	//����� ���������� �� �������� � ���� �� �������
	T back();

	class Iterator
	{
	public:
		Iterator();
		Iterator(Node*);

		T operator*();
		//��������� �������� �� �������������� (it = ++v.begin())
		Iterator& operator++()
		{
			this->current = this->current->getNext();
			return (*this);
		}
		// ���������� �������� �� ��������������(it = v.begin()++)
		Iterator operator++(int)
		{
			Iterator temp = *this;
			++*this;
			return temp;
		}
		//��������� ���� �������� �� ��� Node-a �� ��������
		bool operator!=(const Iterator& temp);
		//������� ������� �� ������� �� ��������� ��� ����� �������
		Node* getCurrent()
		{
			return this->current;
		}
		void setCurrent(Node* temp)
		{
			this->current = temp;
		}

	private:
		Node* current; //�� ������� �������

	friend class List<T>;
	};

	//����� iterator ��� �������� �� �������
	Iterator begin()
	{
		return Iterator(start);
	}
	//����� iterator ��� ���� �� �������(���� ������� ���� ���� �� �������)
	Iterator end()
	{
		return Iterator(end);
	}
	//������ ������� ��� �������� value �� ������� iterator
	void insert(Iterator& it, const T& value); 
	//������� ������� �� ������� iterator
	void erase(Iterator it); 
	//����� ���� �������� � �������
	int getSize(); 
	//������� ������ �������� �� �������
	void clear(); 
	//��������� ���� ������� � ������
	bool empty(); 

private:
	unsigned int size; //����� �� ���������� �� �������
	Node* start;
	Node* end;
};


//���������� �� class List
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

	//���������(��������) �� ������ �����
	current = original.start;
	start = new Node(current->m_data);
	end = start;

	current = current->m_next;
	while (current != NULL)
	{
		//������� �� ��� �����
		ptr_new = new Node(current->m_data);
		end->m_next = ptr_new; //������ �� ���������� � ����� �����
		ptr_new->m_prev = end; //������ �� ����� � ���������� �����
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
	it.setCurrent(insNode); //�� �� ���� �� ���� � ���� �������
}

template<class T>
void List<T>::erase(Iterator it)
{
	if (it.getCurrent()->getPrev() == NULL) // ��������� �� ���� ��������� � � �������� �� �������
	{
		it.setCurrent(it.getCurrent()->getNext());
		it.getCurrent()->setPrev(NULL);
		this->start = it.getCurrent();
	}
	else if (it.getCurrent()->getNext() == NULL) // ��������� �� ���� ��������� � � ���� �� �������
	{
		it.setCurrent(it.getCurrent()->getPrev());
		it.getCurrent()->setNext(NULL);
		this->end = it.getCurrent();
	}
	else                                       // ��� ��������� � � ������� �� �������
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


//���������� �� class Iterator
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