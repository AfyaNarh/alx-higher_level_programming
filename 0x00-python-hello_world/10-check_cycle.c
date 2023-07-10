#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle in it
 * @list: Pointer to the head node of the linked list
 *
 * Return: 0 if no cycle exist, 1 if cycle exists
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
		return (0);

	slow = list;
	fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}

