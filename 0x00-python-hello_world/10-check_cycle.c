#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: input list
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *intlist = list, *nwlist = list;
	int exists = 0;

	while ((intlist && nwlist) && nwlist->next)
	{
		intlist = intlist->next;

		if (nwlist->next || nwlist->next->next)
			nwlist = nwlist->next->next;
		else
			break;

		if (intlist == nwlist)
		{
			exists = 1;
			break;
		}
	}

	return (exists);
}
