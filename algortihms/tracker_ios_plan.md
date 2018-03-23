# GPS Tracker ios

App delegate:

- Talks with os

ViewController:

- main view

Corelocation manager
init
stick on viewcontroller

the delegate recieves events from the location manager

the location manger talks to the os

# no gc
- no GC because will slow down animations
- instead solution is ref count
- if ref count is cyclic then you must use one weak reference
- weak references don't increase ref count
- cycles can happen with more than two objects

startMonitoring: region desiredAcc: acc

    // must be initialized in init
    // other wise will get compile time error
    x = clmanger

    // can be null in the program, I'll handle that
    // checks that you check it is null
    x = clmanager?

    // trust be it won't be null
    // tell the compiler to not bother checking 
    // if we are checking if null
    x = clmanager!

# alamofire

sendData(location, success, error) {
    lib(url + location).responseSuccess {
        return success
    }
}


## Enabling settings

- Blog overview https://www.raywenderlich.com/143128/background-modes-tutorial-getting-started
- Background location in swift https://stackoverflow.com/a/45567876/1376627
- Conforming to delegate https://stackoverflow.com/questions/35900126/cannot-assign-value-of-type-appdelegate-to-type-cllocationmanagerdelegate
