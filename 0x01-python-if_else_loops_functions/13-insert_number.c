#include "lists.h"

/**
 * insert_node - a function in C that inserts a number into a
 * sorted singly linked list.
 *
 * Return: Always 0.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *tmp = NULL;

	if (!head && !*head)
		return (NUll);

	new_node = malloc(sizeof(listint_t))

		if (new_node)
			new_node->n = number;

	tmp = *head;

	while(tmp)
	{
		if (tmp->n > new_node->n)
		{
			new_node->next = tmp;
			tmp = new_node;
		}
		else if (tmp->n < new_node->n && tmp->next->n > new_node->n)
		{
			new_node->next = tmp->next;
			tmp->next = new_node;
		}
		else:
			tmp = tmp->next;
	}
	return (new_node);
}
