<?php

declare(strict_types=1);

namespace App\Temporaring;

use Symfony\Bundle\FrameworkBundle\Kernel\MicroKernelTrait;
use Symfony\Component\HttpKernel\Kernel as BaseKernel;

/**
 * Boots the standalone Symfony runtime used for Temporaring orchestration and verification.
 */
final class Kernel extends BaseKernel
{
    use MicroKernelTrait;
}
