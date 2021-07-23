# API の仕様を記載

## ユーザ情報

1. root

- URI: /users/{user_id}

  ### Get

  - input 情報

    - なし(URI の user_id を元に取得)

  - output 情報

    - ユーザ情報(ユーザ名,ユーザ mail,(いつかユーザ icon))
    - 所属グループ情報(グループ名,グループ ID)

    ```typescript
    type return_body = {
      name: string; //user.name
      mail: string; //user.mail
      groups: {
        name: string; //group.name
        id: string; //group.id
      };
    };
    ```

## グループ情報

1. root

   - URI: /groups/{group_id}

   ### Get

   - input 情報

     - なし(URI の group_id を元に取得)

   - output 情報

     - グループ情報(グループ名,グループ所属ユーザ名,グループ所属ユーザ ID,)

     ```typescript
     type return_body = {
       name: string; //group.name
       id: string; //group.id
       users: [
         {
           name: string; //user.name
           id: string; //user.id
         }
       ];
     };
     ```

   ### Put

   - input 情報

     - ユーザの削除/追加情報
     - グループ名の変更

     ```typescript
     type item_body = {
       name: string; //group.name
       users: [
         {
           id: string; //user.id 今いるユーザのすべて
         }
       ];
     };
     ```

   - output 情報
     - error 情報

2. costs

   - URI: /groups/{group_id}/costs/{yyyyMM}

   ### Get

   - input 情報

     - なし(URI の group_id, yyyyMM を元に取得)

   - output 情報

     - yyyyMM の costs 情報

     ```typescript
     type return_body = [
       {
         date: string; //yyyy/MM/dd
         id: string; //uuid
         value: Decimal; //value
         user: string; //user.name
         category: stiring; //uuid
         comment: string; //comment
       }
     ];
     ```

   ### Post

   - input 情報

     - cost の情報(日付,値段,カテゴリー ID, コメント)

     ```typescript
     type item_body = {
       date: string; //yyyy/MM/dd
       value: Decimal; //value
       category: stiring; //uuid
       comment: string; //commnet
     };
     ```

     - user 情報は jwt から取得！
     - db には id, user_id, group_id を更に追加

   - output 情報

     - error 情報

   ### Put

   - input 情報

     - cost の情報()

     ```typescript
     type item_body = {
       id: string; //uuid
       date: string; //yyyy/MM/dd
       value: Decimal; //value
       category: stiring; //uuid
       comment: string; //commnet
     };
     ```

     - user 情報は jwt から取得！
     - db には user_id, group_id を更に追加

   - output 情報
     - error 情報

   ### delete

   - input 情報

     - 削除する id 情報

     ```typescript
     type item_body = {
       id: string; //uuid
     };
     ```

   - output 情報
     - error 情報

3. categories

   - URI: /groups/{group_id}/categories

   ### Get

   - input 情報

     - なし(URI の group_id を元に取得)

   - output 情報
     - カテゴリー情報(カテゴリ ID, name, index, status)
     ```typescript
     type item_body = [
       {
         id: string; //category.id
         name: string; //category.name
         index: int; //int
         status: boolean; //True=表示しない, False=表示する
       }
     ];
     ```

   ### Post

   - input 情報

     - カテゴリ情報(name)

     ```typescript
     type item_body = {
       name: string; //category.name
     };
     ```

     - API で id, index(latest な番号), status=false(表示しておく)を入れる

   - output 情報
     - error 情報

   ### Put

   - input 情報
   - カテゴリ情報(name, index, status)

   ```typescript
   type item_body = {
     id: string; //category.id
     name: string; //category.name
     index: int; //category.index
     status: boolean; //category.status
   };
   ```

   - output 情報
     - error 情報

4. todos

   - URI: /groups/{group_id}/todos

   ### Get

   - input 情報
     - なし(URI の group_id を元に取得)
   - output 情報

     - todo 情報(id, name, comment, status, user)

       ```typescript
       type return_body = {
         id: string; //todo.id
         name: string; //todo.name
         status: boolean; //todo.status
         user: string; //user.name
         comment: stirng; //comment
       };
       ```

   ### Post

   - input 情報

     - todo 情報(name, comment)

     ```typescript
     type item_body = {
       name: string; //todo.name
       comment: stirng; //comment
     };
     ```

   - output 情報
     - error 情報

   ### Put

   - input 情報

     - todo 情報(id, name, comment, status)

       ```typescript
       type item_body = {
         id: string; //todo.id
         name: string; //todo.name
         status: boolean; //todo.status
         comment: stirng; //comment
       };
       ```

   - output 情報
     - error 情報

   ### Delete

   - input 情報

     - todo 情報(id)

       ```typescript
       type item_body = {
         id: string; //todo.id
       };
       ```

   - output 情報
     - error 情報

5. calendars

   - URI: /groups/{group_id}/calendars

   ### Get

   - input 情報
     - なし(URI の group_id を元に取得)
   - output 情報

     - calendars 情報(id, name, comment, status, start_datetime, end_datetime)

     ```typescript
     type return_body = {
       id: string; //calendar.id
       name: string; //calendar.name
       start_datetime: string; //yyyy/MM/dd
       end_datetime: string; //yyyy/MM/dd
       comment: stirng; //comment
     };
     ```

   ### Post

   - input 情報
     - calendars情報
       ```typescript
       type item_body = {
       name: string; //calendar.name
       start_datetime: string; //yyyy/MM/dd
       end_datetime: string; //yyyy/MM/dd
       comment: stirng; //comment
       };
       ```
    - output情報
        - error 情報

    ### Put
    - input 情報
     - calendars情報
       ```typescript
       type item_body = {
       id: string; // uuid
       name: string; //calendar.name
       start_datetime: string; //yyyy/MM/dd
       end_datetime: string; //yyyy/MM/dd
       comment: stirng; //comment
       };
       ```
    - output情報
        - error 情報
    
    ### Delete
    - input 情報
     - calendars情報
       ```typescript
       type item_body = {
       id: string; // uuid
       };
       ```
    - output情報
        - error 情報
        