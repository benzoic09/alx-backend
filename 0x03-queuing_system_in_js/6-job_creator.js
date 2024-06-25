import kue from 'kue'

const queue = kue.createQueue();

const jobtata = {
    phoneNumber: '1234567890',
    message: 'This is a test notification message'
};

const job = queue.create('push_notification_code', jobtata)
    .save((err) => {
        if (!err) {
            console.log(`Notification job created: ${job.id}`);
        } else {
            console .log('Error creating job:', err);
        }
});
