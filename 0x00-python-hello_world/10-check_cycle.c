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
/**
 * print_listint - prints elements of a linked list
 * *h: elements
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	size_t n_count = 0;
	
	while (h != NULL)
	{
		printf("%d", h->n);
		n_count++;
		if (h->next != NULL)
			printf(" -> ");
		else
			printf("\n");
	}
	h = h->next;
	return (n_count);
}
/**
 * add_nodeint - adds a new node
 * @head: first node
 * n: integer
 * Return: pointer to new head
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));
	
	if (new_node == NULL)
		return NULL;
	new_node->n = n;
	new_node->next = *head;
	*head = new_node;
	return (new_node);
}
/**
 * free_listint - frees the listint
 * @head: first node
 */
void free_listint(listint_t *head)
{
	while (head != NULL)
	{
		listint_t *temp = head;
		head = head->next;
		free(temp);
	}
}
