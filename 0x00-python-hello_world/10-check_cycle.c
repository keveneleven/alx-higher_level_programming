#include "lists.h"

/**
 * check_cycle - checks for a linked lists cycle
 * @lists: list to cycle
 * Return: 0 if there is no cycle
 * and 1 if there is a cycle
 */
int check_cycle(listint_t *lists)
{
	listint_t *fast, *slow = list;
	
	if (list == NULL || list->next == NULL)
		return (0);
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	if (slow == fast)
		return (1);
	return (0);
}
