/* Robert Nusser
 * 14.11.2017
 * location cat:
 * - to find the end location of a file
 *      OR
 * - to jump to a given location and copy contents to stdout from there. */

#include <stdio.h>
#include <stdlib.h>

long pos = 0;
FILE *fp;
char *filename;
char buf[BUFSIZ];

main (int argc, char *argv[])
{
	if (argc == 2 )
		filename = argv[1];
	else if (argc == 3 )
	{
		pos = strtol(argv[1],NULL,10);
		filename = argv[2];
	}
	else
	{
		printf ("Please enter either just a file name, ");
		printf ("or a value to seek to and then the file name.\n");
		printf ("eg: %s 32500 /var/log/messages\n", argv[0]);
		exit(1);
	}

	fp = fopen(filename, "r");
	if (fp == NULL )
	{
		perror("error");
		exit(1);
	}

	
	if (  pos == 0 )
	{		
		fseek(fp, 0L, SEEK_END);
		pos = ftell(fp);
		printf("%ld\n", pos);
		fclose (fp);
		return(0);
	}
	else
	{
		fseek(fp, pos, SEEK_SET);
	        while (fgets(buf, sizeof buf, fp) != NULL)
                	fputs(buf, stdout);

        }
}


