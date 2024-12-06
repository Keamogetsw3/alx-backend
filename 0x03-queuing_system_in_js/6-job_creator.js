import { createQueue } from 'kue';

const queue = createQueue();
const jobData = { phoneNumber: '+2775412522', message: 'Thank you for contacting us.' };
const job = queue.create('push_notification_code', jobData).save((error) => {
  if (!error) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
