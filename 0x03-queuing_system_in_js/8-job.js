#!/usr/bin/node

function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  for (let job of jobs) {
    job = queue.create('push_notification_code_3', job);
    job
      .on('complete', (result) => {
        console.log(`Notification job ${job.id} completed`);
      })
      .on('failed', (err) => {
        console.log(`Notification job ${job.id} failed: ${err.message || err.toString()}`);
      })
      .on('progress', (progress, data) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      })
      .save((err) => {
        console.log(`Notification job created: ${job.id}`);
      });
  }
}
