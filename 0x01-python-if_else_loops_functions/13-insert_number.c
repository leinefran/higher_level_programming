#include "lists.h"

/**
 * insert_node - a function in C that inserts a number into a
 * sorted singly linked list.
 * @head: the pointer to the list.
 * @number: the data store in the new_node.
 * Return: Always 0.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *tmp = NULL;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));

		if (new_node == NULL)
			return (NULL);

		new_node->n = number;
		new_node->next = *head;

		if (*head == NULL)
			*head = new_node;

	tmp = *head;

	while (tmp->next)
	{
		if (tmp->n < new_node->n && tmp->next->n > new_node->n)
		{
			new_node->next = tmp->next;
			tmp->next = new_node;
		}
		tmp = tmp->next;
	}
	return (new_node);
}
