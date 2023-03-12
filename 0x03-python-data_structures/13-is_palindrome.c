#include "lists.h"

/**
 * is_palindrome -  checks if a singly linked list is a palindrome.
 * @head: input
 * Return: success or failure
*/
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	if (is_pal_recurs(*head, *head) != NULL)
		return (1);
	return (0);
}
