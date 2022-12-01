```javascript
let validator = {
    set: function(target, key, value) {
        console.log(`The property ${key} has been updated with ${value}`);
        return true;
    }
};
let store = new Proxy({}, validator);
store.a = 'hello';
// console => The property a has been updated with hello
```
