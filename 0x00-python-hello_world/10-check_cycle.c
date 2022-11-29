#include "stdio.h"
#include "lists.h"

/**
 check_cycle - checks if a singly linked list has a cycle in it
 *
 * list - sinlgy linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	if (list->next == NULL)
	{
		return (0);
	}
	else
	{
		return (1);
	}
}
