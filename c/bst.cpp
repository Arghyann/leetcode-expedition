#include<iostream>
#include<queue>
#include<stack>
using namespace std;
struct node{
    int value;
    struct node* left;
    struct node* right;
}*root=nullptr;
node* last=nullptr;
node* search(node* head,int key){
    last=nullptr;
    while (head!=nullptr){
        last=head;
        if(head->value==key){
            return head;
        }
        else if(head->value<key){
            head=head->right;
        
        }
        else{
            head=head->left;
        }
    }
    return nullptr;

}
void insert(int val){
    node* temp=new node;
    temp->value=val;
    temp->left=nullptr;
    temp->right=nullptr;
    if (root==nullptr){
        
        
        root=temp;
        return;   

    }
    else {node* searched=search(root,val);
    if(searched==nullptr){
        cout<<"value added"<<endl;
        if(val>last->value){
            last->right=temp;

            
            return;
        }
        if(val<last->value){
            
            last->left=temp;
            return;
    }}
    else{cout<<"value already exists"<<endl;}}
}
void BFS(){
    queue <node*> q;
    if(root==nullptr) return;
    q.push(root);
    while(!q.empty()){
        node* current=q.front();
        cout<<current->value<<" ";
        q.pop();
        
        if(current->left!=nullptr) q.push(current->left);
        if(current->right!=nullptr){ q.push(current->right);cout<<"\n";}
        
    }}
void DFS(){
    stack <node*> s;
    if(root==nullptr) return;
    s.push(root);
    while(!s.empty()){
        node* current=s.top();
        while(current->left!=nullptr){
            current=current->left;
            s.push(current);
        }
        


    }
}
int main(){
    int i,num;
    node* smt;
    while (true){
        cout<<"1. Insert \n2. Search \n3. Break\n4. DFS\n5. BFS\n"<<endl;
        cout<<"enter you choice: ";
        cin>>i;
        switch (i)
        {
        case 1:
            cout<<"enter the number you wanna insert: ";
            cin>>num;
            insert(num);
            break;
        case 2:
            cout<<"enter the number to be searched: ";
            cin>>num;
            smt=search(root,num);
            if(smt!=nullptr) cout<<"number found\n";
            else cout<<"not found";
            break;
        case 3:
            return 0;
        case 5:
            BFS();
            break;    
        default:
            break;
        }

    }
}