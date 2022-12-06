#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *prev;
	listint_t *temp;
	listint_t *curr;

	if ((*head)->next == NULL)
		return (1);

	/* find the midle of the list */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	/* Reverse from the midle */
	prev = NULL;
	curr = slow;
	while (curr != NULL)
	{
		temp = curr->next;
		slow->next = prev;
		prev = curr;
		curr = temp;
	}

	/* check the data if it compares */
	while (prev != NULL)
	{
		if ((*head)->n != prev->n)
			return (0);
		*head = (*head)->next;
		prev = prev->next;
	}
	return (1);
}
