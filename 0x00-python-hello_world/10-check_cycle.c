#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: points to the address of the first node.
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next;
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next;
	}
	return (0);
}
