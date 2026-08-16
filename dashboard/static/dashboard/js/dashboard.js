/**
 * CareWell Clinic Admin Dashboard Javascript
 * Handles Chart.js instances, dropdowns, responsiveness & interactions
 */

document.addEventListener('DOMContentLoaded', function () {
  // Mobile Sidebar Drawer Toggle
  const hamburgerBtn = document.getElementById('hamburgerBtn');
  const sidebar = document.getElementById('sidebar');
  const sidebarBackdrop = document.getElementById('sidebarBackdrop');

  function openSidebar() {
    if (sidebar) sidebar.classList.add('open');
    if (sidebarBackdrop) sidebarBackdrop.classList.add('show');
    document.body.style.overflow = 'hidden';
  }

  function closeSidebar() {
    if (sidebar) sidebar.classList.remove('open');
    if (sidebarBackdrop) sidebarBackdrop.classList.remove('show');
    document.body.style.overflow = '';
  }

  if (hamburgerBtn) {
    hamburgerBtn.addEventListener('click', openSidebar);
  }

  if (sidebarBackdrop) {
    sidebarBackdrop.addEventListener('click', closeSidebar);
  }

  // Period Selector Dropdown
  const periodDropdownBtn = document.getElementById('periodDropdownBtn');
  const periodMenu = document.getElementById('periodMenu');
  const currentPeriodText = document.getElementById('currentPeriodText');

  if (periodDropdownBtn && periodMenu) {
    periodDropdownBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      periodMenu.classList.toggle('show');
    });

    document.addEventListener('click', function () {
      periodMenu.classList.remove('show');
    });

    const menuItems = periodMenu.querySelectorAll('.period-menu-item');
    menuItems.forEach(item => {
      item.addEventListener('click', function () {
        const period = this.getAttribute('data-period');
        if (currentPeriodText) {
          currentPeriodText.textContent = this.textContent.trim();
        }
        periodMenu.classList.remove('show');
        fetchPeriodData(period);
      });
    });
  }

  // Date Selector Interaction
  const dateSelectorBtn = document.getElementById('dateSelectorBtn');
  if (dateSelectorBtn) {
    dateSelectorBtn.addEventListener('click', function () {
      const hiddenInput = document.getElementById('datePickerInput');
      if (hiddenInput) {
        hiddenInput.showPicker ? hiddenInput.showPicker() : hiddenInput.focus();
      }
    });
  }

  const datePickerInput = document.getElementById('datePickerInput');
  if (datePickerInput) {
    datePickerInput.addEventListener('change', function () {
      if (this.value) {
        const d = new Date(this.value);
        const options = { month: 'short', day: 'numeric', year: 'numeric' };
        const formatted = d.toLocaleDateString('en-US', options);
        const displayElem = document.getElementById('currentDateText');
        if (displayElem) displayElem.textContent = formatted;
      }
    });
  }

  // Notifications toggle toast
  const notificationBtn = document.getElementById('notificationBtn');
  if (notificationBtn) {
    notificationBtn.addEventListener('click', function () {
      const badge = this.querySelector('.notification-badge');
      if (badge) badge.style.display = 'none';
      alert('You have 3 unread clinic notifications:\n• 2 new patient appointments booked\n• Dr. Brian confirmed dental surgery schedule\n• Monthly revenue report ready');
    });
  }

  // INITIALIZE CHARTS
  initAppointmentsOverviewChart();
  initStatusDoughnutChart();
  initMonthlyRevenueChart();
});

let appointmentsChartInstance = null;

function initAppointmentsOverviewChart() {
  const canvas = document.getElementById('appointmentsOverviewChart');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');

  // Gradient fill for Today dataset
  const gradient = ctx.createLinearGradient(0, 0, 0, 200);
  gradient.addColorStop(0, 'rgba(37, 99, 235, 0.16)');
  gradient.addColorStop(1, 'rgba(37, 99, 235, 0.00)');

  // Data config matching reference
  // X: 8AM, 10AM, 12PM, 2PM, 4PM, 6PM
  const labels = ['8AM', '10AM', '12PM', '2PM', '4PM', '6PM'];
  const todayData = [0, 8, 14, 11, 5, 0];
  const yesterdayData = [0, 3, 6, 4, 3, 0];

  // If server passed custom JSON
  const labelsElem = document.getElementById('chartLabelsData');
  const todayElem = document.getElementById('chartTodayData');
  const yesterdayElem = document.getElementById('chartYesterdayData');

  let finalLabels = labels;
  let finalToday = todayData;
  let finalYesterday = yesterdayData;

  if (labelsElem && todayElem && yesterdayElem) {
    try {
      const parsedLabels = JSON.parse(labelsElem.textContent);
      const parsedToday = JSON.parse(todayElem.textContent);
      const parsedYesterday = JSON.parse(yesterdayElem.textContent);
      if (parsedLabels && parsedToday && parsedYesterday) {
        finalLabels = parsedLabels;
        finalToday = parsedToday;
        finalYesterday = parsedYesterday;
      }
    } catch (e) {
      console.warn('Using default chart dataset', e);
    }
  }

  appointmentsChartInstance = new Chart(ctx, {
    type: 'line',
    data: {
      labels: finalLabels,
      datasets: [
        {
          label: 'Today',
          data: finalToday,
          borderColor: '#2563EB',
          borderWidth: 2.6,
          backgroundColor: gradient,
          fill: true,
          tension: 0.38,
          pointBackgroundColor: '#2563EB',
          pointBorderColor: '#FFFFFF',
          pointBorderWidth: 2,
          pointRadius: 4,
          pointHoverRadius: 6,
        },
        {
          label: 'Yesterday',
          data: finalYesterday,
          borderColor: '#94A3B8',
          borderWidth: 1.8,
          borderDash: [5, 4],
          backgroundColor: 'transparent',
          fill: false,
          tension: 0.38,
          pointBackgroundColor: '#94A3B8',
          pointBorderColor: '#FFFFFF',
          pointBorderWidth: 1.5,
          pointRadius: 3.5,
          pointHoverRadius: 5,
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      interaction: {
        mode: 'index',
        intersect: false,
      },
      plugins: {
        legend: {
          display: false // Using bespoke visual legend header
        },
        tooltip: {
          backgroundColor: '#0F172A',
          titleFont: { family: 'Inter', size: 12, weight: '600' },
          bodyFont: { family: 'Inter', size: 12 },
          padding: 10,
          cornerRadius: 8,
          boxPadding: 4,
        }
      },
      scales: {
        x: {
          grid: {
            display: false,
            drawBorder: false,
          },
          ticks: {
            font: { family: 'Inter', size: 11, weight: '500' },
            color: '#64748B',
            maxRotation: 0,
          }
        },
        y: {
          min: 0,
          max: 20,
          ticks: {
            stepSize: 5,
            font: { family: 'Inter', size: 11 },
            color: '#64748B',
            padding: 8,
          },
          grid: {
            color: '#F1F5F9',
            drawBorder: false,
          },
          border: {
            display: false
          }
        }
      }
    }
  });
}

function fetchPeriodData(period) {
  if (!appointmentsChartInstance) return;

  fetch(`/api/chart-data/?period=${period}`)
    .then(res => res.json())
    .then(data => {
      appointmentsChartInstance.data.labels = data.labels;
      appointmentsChartInstance.data.datasets[0].data = data.today;
      appointmentsChartInstance.data.datasets[1].data = data.yesterday;
      
      const maxVal = Math.max(...data.today, ...data.yesterday);
      appointmentsChartInstance.options.scales.y.max = maxVal > 20 ? Math.ceil(maxVal * 1.15) : 20;
      appointmentsChartInstance.update();
    })
    .catch(err => console.error('Error fetching period data:', err));
}

function initStatusDoughnutChart() {
  const canvas = document.getElementById('appointmentStatusChart');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');

  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Confirmed', 'Completed', 'Pending', 'Cancelled'],
      datasets: [{
        data: [22, 12, 6, 2],
        backgroundColor: [
          '#2563EB', // Confirmed Blue
          '#22C55E', // Completed Green
          '#F59E0B', // Pending Orange
          '#EF4444', // Cancelled Red
        ],
        borderWidth: 2.5,
        borderColor: '#FFFFFF',
        hoverOffset: 4,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      cutout: '72%',
      plugins: {
        legend: {
          display: false
        },
        tooltip: {
          backgroundColor: '#0F172A',
          titleFont: { family: 'Inter', size: 12, weight: '600' },
          bodyFont: { family: 'Inter', size: 12 },
          padding: 10,
          cornerRadius: 8,
          callbacks: {
            label: function (context) {
              const total = 42;
              const val = context.raw;
              const pct = Math.round((val / total) * 100);
              return ` ${context.label}: ${val} (${pct}%)`;
            }
          }
        }
      }
    }
  });
}

function initMonthlyRevenueChart() {
  const canvas = document.getElementById('monthlyRevenueChart');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');

  const labelsElem = document.getElementById('revLabelsData');
  const valuesElem = document.getElementById('revValuesData');

  let labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May'];
  let values = [85000, 100000, 102000, 120000, 125600];

  if (labelsElem && valuesElem) {
    try {
      labels = JSON.parse(labelsElem.textContent);
      values = JSON.parse(valuesElem.textContent);
    } catch (e) {
      console.warn('Using default revenue values', e);
    }
  }

  // Highlight May (current month) in green, others in soft blue
  const backgroundColors = values.map((val, idx) => {
    return idx === values.length - 1 ? '#22C55E' : '#93C5FD';
  });

  const hoverColors = values.map((val, idx) => {
    return idx === values.length - 1 ? '#16A34A' : '#60A5FA';
  });

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Revenue (KES)',
        data: values,
        backgroundColor: backgroundColors,
        hoverBackgroundColor: hoverColors,
        borderRadius: 4,
        borderSkipped: false,
        barPercentage: 0.52,
        categoryPercentage: 0.75,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false
        },
        tooltip: {
          backgroundColor: '#0F172A',
          titleFont: { family: 'Inter', size: 12, weight: '600' },
          bodyFont: { family: 'Inter', size: 12 },
          padding: 10,
          cornerRadius: 8,
          callbacks: {
            label: function (context) {
              return ` Revenue: KES ${context.raw.toLocaleString()}`;
            }
          }
        }
      },
      scales: {
        x: {
          grid: {
            display: false,
            drawBorder: false,
          },
          ticks: {
            font: { family: 'Inter', size: 11, weight: '500' },
            color: '#64748B',
          }
        },
        y: {
          min: 0,
          max: 150000,
          ticks: {
            stepSize: 50000,
            font: { family: 'Inter', size: 10.5 },
            color: '#64748B',
            callback: function (value) {
              if (value === 0) return '0';
              return (value / 1000) + 'K';
            }
          },
          grid: {
            color: '#F1F5F9',
            drawBorder: false,
          },
          border: {
            display: false
          }
        }
      }
    }
  });
}
