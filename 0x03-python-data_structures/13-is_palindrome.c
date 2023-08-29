#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - reverses a singly linked list
 * @head: head of the list
 * Return: head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *previous = NULL;

	while (node)
	{
		next = node->next;
		node->next = previous;
		previous = node;
		node = next;
	}

	*head = previous;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of the list
 * Return: If not a palindrome 0
 * otherwise -1
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *reverse, *middle;
	size_t size = 0, m;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (m = 0; m < (size / 2) - 1; m++)
		temp = temp->next;

	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	reverse = reverse_listint(&temp);
	middle = reverse;

	temp = *head;
	while (reverse)
	{
		if (temp->n != reverse->n)
			return (0);
		temp = temp->next;
		reverse = reverse->next;
	}
	reverse_listint(&middle);

	return (1);
}
