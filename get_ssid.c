#include <stdio.h>
#include <stdlib.h>

#define EXIT_FAILURE -1
// #define SSID "NUS_STU"

void get_ssid() {

}

int main() {
	FILE* fp = fopen("network.out", "r"), of = fopen("list.out", "a");
	char input[100];

	if(!fp) {
		perror("File opening failed");
		return EXIT_FAILURE;
	}

	if(!of) {
		perror("File writing failed");
		return -2;
	}


	if( fgets (str, 60, fp) != NULL ) {
      /* writing content to stdout */
		fgets(input, 100, fp);
		if (strstr(input, "SSID") != NULL)
			break;
	}

	strstr()


	return 0;
}