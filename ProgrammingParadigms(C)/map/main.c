#include <search.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>


void* resultMap = NULL;
void* tmpMap = NULL;

typedef struct
{
      char* key;
      int value;
} strIntNode;

int getValueFromNode(void* node) {
    return (*(strIntNode**)node) -> value;
}

char* getKeyFromNode(void* node) {
    return (*(strIntNode**)node) -> key;
}

// create map
void* createMap() {
    return 0;
}


// comparator for binary tree
int compar(const void *l, const void *r)
{
    const strIntNode *lm = l;
    const strIntNode *lr = r;
    return strcmp(lm->key, lr->key);
}

// find
void* findEl(void** root, char* key) {
    strIntNode* element = malloc(sizeof(strIntNode));
    element -> key = key;
    void* searchResult = tfind(element, root, compar);
    // int result = (*(strIntNode**)searchResult) -> value;
    return searchResult;
}

// delete
void removeEl(void** root, char* key) {
    strIntNode* element = malloc(sizeof(strIntNode));
    element -> key = key;
    tdelete(element, root, compar);
}

// insert
void* insertEl(void** root, char* key, int value) {
    if (findEl(root, key) != NULL) {
        removeEl(root, key);
    }
    strIntNode* element = malloc(sizeof(strIntNode));
    element -> key = key;
    element -> value = value;
    void* result = tsearch(element, root, compar);
    return result;
}

void actionInsert(const void *nodep, VISIT which, int depth)
{
   char* key;
   int value;

   switch (which) {
   case preorder:
       key = getKeyFromNode(nodep);
       value = getValueFromNode(nodep);
       /*
       printf("1st time: key %s  value %d \n", key, value);
       */
       break;
   case postorder:

       key = getKeyFromNode(nodep);
       value = getValueFromNode(nodep);
       /*
       printf("2nd time: key %s  value %d \n", key, value);
       */
       insertEl(&resultMap, key, value);
       break;
   case endorder:
       /*
       key = getKeyFromNode(nodep);
       value = getValueFromNode(nodep);
       printf("3rd time: key %s  value %d \n", key, value);
       */
       break;
   case leaf:
       key = getKeyFromNode(nodep);
       value = getValueFromNode(nodep);
       /*
       printf("leaf: key %s  value %d \n", key, value);
       */
       insertEl(&resultMap, key, value);
       break;
   }
}

void actionPrint(const void *nodep, VISIT which, int depth)
{
   char* key;
   int value;

   switch (which) {
   case preorder:
       break;
   case postorder:
       key = getKeyFromNode(nodep);
       value = getValueFromNode(nodep);
       printf("key %s  value %d \n", key, value);
       break;
   case endorder:
       break;
   case leaf:
       key = getKeyFromNode(nodep);
       value = getValueFromNode(nodep);
       printf("key %s  value %d \n", key, value);
       break;
   }
}

void actionCopyToTmp(const void *nodep, VISIT which, int depth)
{
   char* key;
   int value;

   switch (which) {
   case preorder:
       break;
   case postorder:
       key = getKeyFromNode(nodep);
       value = getValueFromNode(nodep);
       insertEl(&tmpMap, key, value);
       break;
   case endorder:
       break;
   case leaf:
       key = getKeyFromNode(nodep);
       value = getValueFromNode(nodep);
       insertEl(&tmpMap, key, value);
       break;
   }
}

void actionCopyToRes(const void *nodep, VISIT which, int depth)
{
   char* key;
   int value;

   switch (which) {
   case preorder:
       break;
   case postorder:
       key = getKeyFromNode(nodep);
       value = getValueFromNode(nodep);
       insertEl(&resultMap, key, value);
       break;
   case endorder:
       break;
   case leaf:
       key = getKeyFromNode(nodep);
       value = getValueFromNode(nodep);
       insertEl(&resultMap, key, value);
       break;
   }
}

void actionFindIntersection(const void *nodep, VISIT which, int depth)
{
   char* key;
   int value;

   switch (which) {
   case preorder:
       break;
   case postorder:
       key = getKeyFromNode(nodep);
       value = getValueFromNode(nodep);
       if (findEl(&tmpMap, key) != NULL) {
            insertEl(&resultMap, key, value);
       }
       break;
   case endorder:
       break;
   case leaf:
       key = getKeyFromNode(nodep);
       value = getValueFromNode(nodep);
       if (findEl(&tmpMap, key) != NULL) {
            insertEl(&resultMap, key, value);
       }
       break;
   }
}

void actionFindDiff(const void *nodep, VISIT which, int depth)
{
   char* key;
   int value;

   switch (which) {
   case preorder:
       break;
   case postorder:
       key = getKeyFromNode(nodep);
       value = getValueFromNode(nodep);
       if (findEl(&resultMap, key) == NULL) {
            insertEl(&resultMap, key, value);
       } else {
            removeEl(&resultMap, key);
       }
       break;
   case endorder:
       break;
   case leaf:
       key = getKeyFromNode(nodep);
       value = getValueFromNode(nodep);
       if (findEl(&resultMap, key) == NULL) {
            insertEl(&resultMap, key, value);
       } else {
            removeEl(&resultMap, key);
       }
       break;
   }
}


// tree union
void* mapUnion(void* thisRoot, void* thatRoot) {
    resultMap = NULL;
    tmpMap = NULL;

    twalk(thisRoot, actionInsert);
    twalk(thatRoot, actionInsert);
    return resultMap;
}

void* mapIntersection(void* thisRoot, void* thatRoot) {
    resultMap = NULL;
    tmpMap = NULL;

    twalk(thisRoot, actionCopyToTmp);
    twalk(thatRoot, actionFindIntersection);
    return resultMap;
}

void* mapDiff(void* thisRoot, void* thatRoot) {
    resultMap = NULL;
    tmpMap = NULL;

    twalk(thatRoot, actionCopyToRes);
    twalk(thisRoot, actionFindDiff);
    return resultMap;
}

int main(int argc, char **argv)
{

    void *mapA = createMap();
    void *mapB = createMap();


    insertEl(&mapA, "key1", 11);
    insertEl(&mapA, "key2", 33);
    insertEl(&mapA, "key3", 44);

    insertEl(&mapB, "key1", 22);
    insertEl(&mapB, "key2", 55);
    insertEl(&mapB, "key4", 66);
    insertEl(&mapB, "key5", 77);

    removeEl(&mapB, "key5");

    void* composedMap = mapUnion(mapA, mapB);
    printf("Merged tree \n");
    twalk(composedMap, actionPrint);

    void* intersectionMap = mapIntersection(mapA, mapB);

    printf("Intersection tree \n");
    twalk(intersectionMap, actionPrint);


    void* diffMap = mapDiff(mapA, mapB);

    printf("Diff tree \n");
    twalk(diffMap, actionPrint);

    return 0;
}
